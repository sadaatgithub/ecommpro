from django.urls import path
from .views import CustomLoginView,HomeView
from django.contrib.auth.views import LogoutView




# app_name = 'account'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='app:home'), name='logout'),


]