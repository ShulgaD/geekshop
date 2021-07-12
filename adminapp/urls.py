"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('/', adminapp.index,
         name='index'),
    path('user/delete/<int:user_pk>/', adminapp.user_delete,
         name='user_delete'),
    path('user/update/<int:user_pk>/', adminapp.ShopUserAdminUpdate.as_view(),
         name='user_update'),
    path('categories/', adminapp.ProductCategoryList.as_view(),
         name='categories'),
    path('category/create/', adminapp.ProductCategoryCreate.as_view(),
         name='category_create'),
    path('category/update/<int:pk>/', adminapp.ProductCategoryUpdate.as_view(),
         name='category_update'),
    path('category/delete/<int:pk>/', adminapp.ProductCategoryDelete.as_view(),
         name='category_delete'),
    path('category/<int:pk>/products/', adminapp.category_products,
         name='category_products'),
    path('category/<int:category_pk>/product/create/', adminapp.category_product_create,
         name='category_product_create'),
    path('product/<int:pk>/', adminapp.ProductDetail.as_view(),
         name='product_view'),

]
