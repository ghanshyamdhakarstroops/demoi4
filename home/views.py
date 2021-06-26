from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .authentications import *



# Create your views here.
# @login_required
def home(request):
	return render(request, 'home.html')

@logout_required
def signup(request):
	if request.method == 'POST':
		username = request.POST.get('name')
		phone = request.POST.get('phone')
		email = request.POST.get('email')
		password = request.POST.get('password1')
		confirm_passowrd = request.POST.get('password2')

		user = User.objects.filter(username = username).first()
		if user:
			messages.info(request, 'User already exists..!')
			return redirect('home:signup')
		else:
			if password != confirm_passowrd:
				messages.info(request, 'Password mismatch')
				return redirect('home:signup')
			else:
				if User.objects.filter(email = email).exists():
					messages.info(request, 'Email already exists....!')
					return redirect('home:signup')
				elif User.objects.filter(phone = phone).exists():
					messages.info(request, 'Phone already exists....!')
					return redirect('home:signup')
				else:
					User.objects.create_user(username = username, email = email, phone = phone, password = password)
					c_user = authenticate(username = username, password=password)
					login(request, c_user)
					return redirect('home:home')
	return render(request, 'signup.html')

@login_required
def profile(request):
	return render(request, 'profile.html')
