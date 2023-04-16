from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages

from .forms import UserRegistrationForm

# Create your views here.

def register_request(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		print(form)
		if form.is_valid():
			form.save()
			
			messages.success(request, f'Your account has been created. You can log in now!')
			return redirect('login')
	else:
		form = UserRegistrationForm()
		
	context = {'form': form}
	return render(request, 'auth/register.html', context)

def main_request(request):
	if request.method == 'GET':
		return render(request, 'main.html')

"""def login_request(request):
	print(request)
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="auth/login.html", context={"login_form":form})"""
