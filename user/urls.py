from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from . import views

urlpatterns = [
    path('', views.main_request, name="raiz"),
    path("register", views.register_request, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page=reverse_lazy('raiz'), template_name='auth/logout.html'), name='logout'),
]