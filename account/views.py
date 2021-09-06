from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from app import views



# Create your views here.


class HomeView(LoginRequiredMixin,TemplateView):
    
    template_name = 'home/index.html'


class CustomLoginView(LoginView):
    template_name = 'app/account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('app:home')