from django.urls import path
from .views import *
from stock import views




app_name='stock'
urlpatterns = [
   path('base', views.base, name='base'),
   path('add_items/', views.add_items, name='add_items'),
   path('list_item/', views.list_item, name='list_item'),
   path('update_items/<str:pk>/', views.update_items, name="update_items"),
   path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
   path('issue_items/<str:pk>/', views.issue_items, name="issue_items"),
   path('receive_items/<str:pk>/', views.receive_items, name="receive_items"),
   path('reorder_level/<str:pk>/', views.reorder_level, name="reorder_level"),
   path('menu_items/<str:pk>/', views.menu_items, name="menu_items"),
   path('add_menu/', views.add_menu, name="add_menu"),
   path('menu/', views.menu, name='menu'),
   

]
 
