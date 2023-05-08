from django.shortcuts import render, get_object_or_404
from user.models import Consultorio, Paciente, Enfermedad, Cita, Consulta
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test

# Create your views here.

def home(request):
	if request.method == 'GET':
		return render(request, 'home.html')

@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def index_sintoma(request):
	if request.method == 'GET':
		return render(request, 'lists/list-sintomas.html')
	
@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def index_signo(request):
	if request.method == 'GET':
		return render(request, 'lists/list-signos.html')
	
@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def index_pruebas(request):
	if request.method == 'GET':
		return render(request, 'lists/list-pruebas.html')
	
@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def index_roles(request):
	if request.method == 'GET':
		return render(request, 'lists/list-roles.html')
	
@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def index_permisos(request):
	if request.method == 'GET':
		return render(request, 'lists/list-permisos.html')

# Vistas de consultorio

@user_passes_test(lambda u: any(group in ['administrador', 'secretario'] for group in u.groups.values_list('name', flat=True)))
def index_consultorio(request):
	if request.method == 'GET':
		return render(request, 'lists/list-consultorios.html')

@user_passes_test(lambda u: any(group in ['administrador', 'secretario'] for group in u.groups.values_list('name', flat=True)))
def create_consultorio(request):
	if request.method == 'GET':
		return render(request, 'forms/form-consultorio.html')

@user_passes_test(lambda u: any(group in ['administrador', 'secretario'] for group in u.groups.values_list('name', flat=True)))
def edit_consultorio(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Consultorio, id=id)
		return render(request, 'forms/form-consultorio.html', {'consultorio': objecto})

# Vistas de paciente

@user_passes_test(lambda u: any(group in ['administrador', 'secretario', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def index_paciente(request):
	if request.method == 'GET':
		return render(request, 'lists/list-pacientes.html')
	
@user_passes_test(lambda u: any(group in ['administrador', 'secretario', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def create_paciente(request):
	if request.method == 'GET':
		return render(request, 'forms/form-paciente.html')

@user_passes_test(lambda u: any(group in ['administrador', 'secretario', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def edit_paciente(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Paciente, id=id)
		return render(request, 'forms/form-paciente.html', {'paciente': objecto})

@user_passes_test(lambda u: any(group in ['administrador', 'secretario', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def ver_historial(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Paciente, id=id)
		return render(request, 'lists/list-historial.html', {'paciente': objecto})

# Vistas de usuario

@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def index_usuario(request):
	if request.method == 'GET':
		return render(request, 'lists/list-usuarios.html')
	
@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def create_usuario(request):
	if request.method == 'GET':
		return render(request, 'forms/form-usuario.html')

@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())	
def edit_usuario(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(User, id=id)
		return render(request, 'forms/form-usuario.html', {'usuario': objecto})
	
# Vistas de enfermedad

@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def index_enfermedad(request):
	if request.method == 'GET':
		return render(request, 'lists/list-enfermedades.html')
	
@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def create_enfermedad(request):
	if request.method == 'GET':
		return render(request, 'forms/form-enfermedad.html')
	
@user_passes_test(lambda u: u.groups.filter(name='administrador').exists())
def edit_enfermedad(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Enfermedad, id=id)
		return render(request, 'forms/form-enfermedad.html', {'enfermedad': objecto})
	
# Vistas de cita

@user_passes_test(lambda u: any(group in ['administrador', 'secretario', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def index_cita(request):
	if request.method == 'GET':
		return render(request, 'lists/list-citas.html')

@user_passes_test(lambda u: any(group in ['administrador', 'secretario', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def create_cita(request):
	if request.method == 'GET':
		return render(request, 'forms/form-cita.html')

@user_passes_test(lambda u: any(group in ['administrador', 'secretario', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def edit_cita(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Cita, id=id)
		return render(request, 'forms/form-cita.html', {'cita': objecto})
	
# Vistas de consulta

@user_passes_test(lambda u: any(group in ['administrador', 'doctor'] for group in u.groups.values_list('name', flat=True)))
def create_consulta(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Cita, id=id)
		return render(request, 'forms/form-consulta.html', {'cita': objecto})
