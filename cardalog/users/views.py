from django.contrib.auth import login
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView

# Custom Sign Up View
class SignUpView(CreateView):
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
	form_class = UserRegisterForm

	# Dealing with Post requests
	def post(self, request, *args, **kwargs):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			user.refresh_from_db() # This brings the profile from db
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.gender = form.cleaned_data.get('gender')
			user.profile.country = form.cleaned_data.get('country')
			user.save()
			messages.success(request, f'Your account has been created! You are now able to log in!')

		return redirect('login')

	# Dealing with Get requests
	def get(self, request, *args, **kwargs):
		form = UserRegisterForm()
		return render(request, 'registration/register.html', {'form': form})

# Custom LoginView
class MyLoginView(SuccessMessageMixin, LoginView):
	template_name = 'registration/login.html'
	success_url = reverse_lazy('cardalog-home')
	success_message = "Welcome back"

# Profile View (My Page)
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # Instance will tell which instance we are working on
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('cardalog-home')
	else:
		u_form = UserUpdateForm(instance=request.user) # Instance will bring current user data
		p_form = ProfileUpdateForm(instance=request.user.profile)
	
	context = {
        'u_form': u_form,
		'p_form': p_form,
    }
	
	return render(request, 'profile.html', context)