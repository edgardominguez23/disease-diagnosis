from django.shortcuts import render, get_object_or_404
from user.models import Consultorio, Paciente

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
