from django.contrib import admin
from django.urls import path, include
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.CategoryList.as_view()),
    path('product-by-category-list/<int:pk>/',
         views.ProductByCategoryList.as_view()),
    path('product-name-by-category-list/<int:pk>/',
         views.ProductNameByCategoryList.as_view()),
]
