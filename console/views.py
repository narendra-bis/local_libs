from django.shortcuts import render,redirect,reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from console.forms import SignUpForm
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.http import HttpResponseRedirect

# Create your views here.


def signout(request):
	logout(request)
	return redirect(reverse('catalog:index'))


def register(request):
	if request.method=='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.genre = form.cleaned_data.get('genre')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.save()
			messages.success(request,_('User registered successfully'))
			return HttpResponseRedirect(reverse('login')) 			
	else:
		form = SignUpForm()
	return render(request,'console/register.html',{'form':form})