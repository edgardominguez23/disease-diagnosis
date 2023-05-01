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
    path("consultorios/create", login_required(views.create_consultorio), name="consultorios-create"),
    path("consultorios/edit/<int:id>/", login_required(views.edit_consultorio), name="consultorios-edit"),

    path("pacientes", login_required(views.index_paciente), name="pacientes-list"),
    path("pacientes/create", login_required(views.create_paciente), name="pacientes-create"),
    path("pacientes/edit/<int:id>/", login_required(views.edit_paciente), name="pacientes-edit"),

    path("usuarios", login_required(views.index_usuario), name="usuarios-list"),
    path("usuarios/create", login_required(views.create_usuario), name="usuarios-create"),
    path("usuarios/edit/<int:id>/", login_required(views.edit_usuario), name="usuarios-edit"),

    path("roles", login_required(views.index_roles), name="roles-list"),
    path("permisos", login_required(views.index_permisos), name="permisos-list"),
]