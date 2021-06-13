from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout 

# Create your views here.


def signout(request):
	logout(request)
	return redirect(reverse('catalog:index'))


def register(request):
	return render(request,'console/register.html')