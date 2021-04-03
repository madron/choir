from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(auth_views.LoginView):
    template_name = 'authentication/login.html'

    def get_success_url(self):
        return reverse('home')


class LogoutView(auth_views.LogoutView):
    def get_next_page(self):
        return reverse('home')
