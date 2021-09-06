from django.urls import path
from .import views


app_name ='app'

urlpatterns = [
    path('',views.home, name="home"),
    path('all_products/',views.all_products, name="all_products"),
    path('item/<slug:slug>/', views.ProductDetail, name="ProductDetail"),
    path('search/<slug:category_slug>/', views.category_list, name="category_list"),
]