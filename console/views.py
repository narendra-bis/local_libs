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

"""
Function for user registration
"""
def register(request):
	if request.method=='POST':
		# import pdb;pdb.set_trace()

		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.genre = form.cleaned_data.get('genre')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.role = form.cleaned_data.get('role')
			user.save()
			messages.success(request,_('User registered successfully'))
			return HttpResponseRedirect(reverse('login')) 			
	else:
		form = SignUpForm()
	return render(request,'console/register.html',{'form':form})

"""

	<div class="input-group">
                            <div class="rs-select2 js-select-simple select--no-search">
                                <select name="role">
                                    <option disabled="disabled" selected="selected">SELECT ROLE</option>
                                    <option value="librarian">Admin</option>
                                    <option value="libuser">Library User</option>
                                    <option value="libstaff">Library Staff</option>
                                </select>
                                <div class="select-dropdown"></div>
                            </div>
                        </div>
 
Assign a user to groups
doctor_group.user_set.add(user)
            OR
user.groups.add(doctor_group)

 """

