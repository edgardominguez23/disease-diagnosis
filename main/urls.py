from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path("", login_required(views.home), name="home"),
    path("sintomas", login_required(views.index_sintoma), name="sintomas-list"),
    path("signos", login_required(views.index_signo), name="signos-list"),
    path("pruebas", login_required(views.index_pruebas), name="pruebas-list"),
    path("consultorios", login_required(views.index_consultorio), name="consultorios-list"),
    path("pacientes", login_required(views.index_paciente), name="pacientes-list"),
]