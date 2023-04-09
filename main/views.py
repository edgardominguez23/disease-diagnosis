from django.shortcuts import render

# Create your views here.

def home_request(request):
	if request.method == 'GET':
		return render(request, 'home.html')
