from django.urls import path

from .views import login_view, RegisterView, register_view, logout_view, LogoutView, ProfileView, AddressView, \
    remove_address, FullNameView, create_address, change_image, OrdersView, ShopDetailView, create_name

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('addresses/', AddressView.as_view(), name='addresses'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('fullname/', FullNameView.as_view(), name='fullname'),
    path('remove_address/', remove_address, name='remove_address'),
    path('create_address/', create_address, name='create_address'),
    path('create_name/', create_name, name='create_name'),
    path('change_image/', change_image, name='change_image'),
    path('shop_detail/<slug:slug>/', ShopDetailView.as_view(), name='shop_detail'),
]
