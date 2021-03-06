import json

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, TemplateView, DetailView
from django.contrib.auth.views import LogoutView

# Create your views here.

# class LoginView(FormView):
#     template_name = 'login.html'
#     form_class = ContactForm
#     success_url = '/'
import product
from account.forms import UserRegistrationForm, UserLoginForm, AddressForm, ImageForm, EditNameForm
from account.models import User, Address, Shop
from order.models import BasketItem, Basket, Order
from product.models import Category, Product, Brand


def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print("form : ", form)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user and user.is_active:
                login(request, user)
                return redirect('home')
        else:
            pass
        context = {'form': form, 'categories': Category.objects.all()}
        print(form.is_valid())
    else:
        form = UserLoginForm()
        context = {'form': form, 'categories': Category.objects.all()}
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


class LogoutView(LogoutView):
    redirect_field_name = '/login/'


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = User.objects.create(email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            # user = form.save(commit=False)
            # password = user.password
            # user.set_password(password)
            # user.save()
            return redirect('login')
        else:
            pass
        context = {'form': form, 'categories': Category.objects.all()}
    else:
        form = UserRegistrationForm()
        context = {'form': form, 'categories': Category.objects.all()}
    return render(request, 'account/register.html', context)


class RegisterView(TemplateView):
    template_name = "account/register.html"


class ProfileView(TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        if self.request.user.is_authenticated:
            context['basket_items'] = BasketItem.objects.filter(basket__user=self.request.user)
            context['basket'] = Basket.objects.get(user=self.request.user)
        return context


class FullNameView(TemplateView):
    template_name = "account/full_name.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        context['categories'] = Category.objects.all()
        if self.request.user.is_authenticated:
            context['basket_items'] = BasketItem.objects.filter(basket__user=self.request.user)
            context['basket'] = Basket.objects.get(user=self.request.user)
        context['brands'] = Brand.objects.all()
        context['form'] = EditNameForm()
        print('form : ', context['form'])
        return context


class AddressView(TemplateView):
    template_name = "account/addresses.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print('kwargs : ', kwargs)
        context['addresses'] = Address.objects.filter(user=self.request.user)
        context['categories'] = Category.objects.all()
        context['basket_items'] = BasketItem.objects.filter(basket__user=self.request.user)
        context['basket'] = Basket.objects.get(user=self.request.user)
        context['brands'] = Brand.objects.all()
        return context


class OrdersView(TemplateView):
    template_name = "account/orders.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        print('kwargs : ', kwargs)
        context['categories'] = Category.objects.all()
        context['basket_items'] = BasketItem.objects.filter(basket__user=self.request.user)
        context['basket'] = Basket.objects.get(user=self.request.user)
        context['orders'] = Order.objects.filter(user=self.request.user)
        context['brands'] = Brand.objects.all()
        return context


class ShopDetailView(DetailView):
    model = Shop
    template_name = "account/shop_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = list(
            map(self.get_min_price, Product.objects.filter(shop_product__shop__slug=self.kwargs['slug'])))
        context['shop'] = Shop.objects.get(slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['basket'] = self.get_basket_basket_items()[0]
        context['basket_items'] = self.get_basket_basket_items()[1]
        return context

    def get_basket_total_price(self, basket_items):
        total_price = 0
        for basket_item in basket_items:
            total_price += basket_item.total
        return total_price

    def get_quatity_of_shop_product(self, shop_products):
        quantity = 0
        for i in shop_products:
            quantity += i.quantity
        return quantity

    def get_basket_basket_items(self):
        if self.request.user.is_authenticated:
            basket = Basket.objects.get(user=self.request.user)
            basket_items = BasketItem.objects.filter(basket__user=self.request.user)
            basket.total_price = self.get_basket_total_price(basket_items)
            basket.save()
            return [basket, basket_items]
        elif Basket.objects.get(user=self.request.user.is_anonymous):
            basket = Basket.objects.get(user=self.request.user.is_anonymous)
            basket_items = BasketItem.objects.filter(basket__user=self.request.user.is_anonymous)
            basket.total_price = self.get_basket_total_price(basket_items)
            basket.save()
            return [basket, basket_items]
        else:
            basket = Basket.objects.create(user=self.request.user.is_anonymous)
            basket_items = []
            basket.total_price = self.get_basket_total_price(basket_items)
            basket.save()
            return [basket, basket_items]

    def get_min_price(self, product):
        min_price = min(item.price for item in product.shop_product.all())
        print("min_price : ", min_price)
        return [product, min_price]


@csrf_exempt
def remove_address(request):
    data = json.loads(request.body)
    try:
        Address.objects.get(id=data['address_id']).delete()
        response = {'address_id': data['address_id']}
        return HttpResponse(json.dumps(response), status=201)
    except:
        response = {'error': 'Error'}
        return HttpResponse(json.dumps(response), status=400)


@csrf_exempt
def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
        print(address)
    return redirect('addresses')


@csrf_exempt
def create_name(request):
    print('request : ', request)
    if request.method == 'POST':
        form = EditNameForm(request.POST)
        print('form ; ', form)
        if form.is_valid():
            user = form.save(commit=False)
            user.user = request.user
            user.save()
        print(user)
    return redirect('fullname')


@csrf_exempt
def change_image(request):
    print('before post')
    data = json.loads(request.body)
    if request.method == 'POST':
        print('after post')
        form = ImageForm(request.POST, request.FILES, instance=request.user)
        print('first_form : ', form)
        if form.is_valid():
            form.save()
            print('second_form : ', form)
            response = {'image': form.image.url}
        else:
            response = {'image': form.image.url}
    return HttpResponse(json.dumps(response), status=201)
