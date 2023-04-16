from django.shortcuts import render

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
	
def index_paciente(request):
	if request.method == 'GET':
		return render(request, 'lists/list-pacientes.html')
