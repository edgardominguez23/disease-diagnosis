from django.shortcuts import render, get_object_or_404
from user.models import Consultorio, Paciente, Enfermedad, Cita, Consulta
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	if request.method == 'GET':
		return render(request, 'home.html')
	
def index_sintoma(request):
	if request.method == 'GET':
		return render(request, 'lists/list-sintomas.html')
	
def index_signo(request):
	if request.method == 'GET':
		return render(request, 'lists/list-signos.html')
	
def index_pruebas(request):
	if request.method == 'GET':
		return render(request, 'lists/list-pruebas.html')
	
def index_roles(request):
	if request.method == 'GET':
		return render(request, 'lists/list-roles.html')
	
def index_permisos(request):
	if request.method == 'GET':
		return render(request, 'lists/list-permisos.html')

# Vistas de consultorio

def index_consultorio(request):
	if request.method == 'GET':
		return render(request, 'lists/list-consultorios.html')
	
def create_consultorio(request):
	if request.method == 'GET':
		return render(request, 'forms/form-consultorio.html')
	
def edit_consultorio(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Consultorio, id=id)
		return render(request, 'forms/form-consultorio.html', {'consultorio': objecto})

# Vistas de paciente

def index_paciente(request):
	if request.method == 'GET':
		return render(request, 'lists/list-pacientes.html')
	
def create_paciente(request):
	if request.method == 'GET':
		return render(request, 'forms/form-paciente.html')
	
def edit_paciente(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Paciente, id=id)
		return render(request, 'forms/form-paciente.html', {'paciente': objecto})

# Vistas de usuario

def index_usuario(request):
	if request.method == 'GET':
		return render(request, 'lists/list-usuarios.html')
	
def create_usuario(request):
	if request.method == 'GET':
		return render(request, 'forms/form-usuario.html')
	
def edit_usuario(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(User, id=id)
		return render(request, 'forms/form-usuario.html', {'usuario': objecto})
	
# Vistas de enfermedad

def index_enfermedad(request):
	if request.method == 'GET':
		return render(request, 'lists/list-enfermedades.html')
	
def create_enfermedad(request):
	if request.method == 'GET':
		return render(request, 'forms/form-enfermedad.html')
	
def edit_enfermedad(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Enfermedad, id=id)
		return render(request, 'forms/form-enfermedad.html', {'enfermedad': objecto})
	
# Vistas de cita

def index_cita(request):
	if request.method == 'GET':
		return render(request, 'lists/list-citas.html')
	
def create_cita(request):
	if request.method == 'GET':
		return render(request, 'forms/form-cita.html')
	
def edit_cita(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Cita, id=id)
		return render(request, 'forms/form-cita.html', {'cita': objecto})
	
# Vistas de consulta

def index_consulta(request):
	if request.method == 'GET':
		return render(request, 'lists/list-consultas.html')
	
def create_consulta(request):
	if request.method == 'GET':
		return render(request, 'forms/form-consulta.html')
	
def edit_consulta(request, id):
	if request.method == 'GET':
		objecto = get_object_or_404(Consulta, id=id)
		return render(request, 'forms/form-consulta.html', {'consulta': objecto})
