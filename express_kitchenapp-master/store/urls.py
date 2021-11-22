from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView, add_stock



app_name='store'

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store/', store , name='store'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('store_list/', OrderView.as_view(), name='store_list'),
    path('add_orders/', add_stock, name='add_stock'),
    # path('store_list/',store_list,name='store_list'),

]
