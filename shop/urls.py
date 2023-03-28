from django.contrib import admin
from django.urls import path
from . import views
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<slug:category_slug>/<slug:subcategory_slug>/', views.product_list_by_subcategory,
         name='product_list_by_subcategory'),
    path('<slug:category_slug>/<slug:subcategory_slug>/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]