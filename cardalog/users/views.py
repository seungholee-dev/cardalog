import json
from django.core.mail import message, send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import authenticate, login
from django.http import response, HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView


# Custom Sign Up View
class SignUpView(CreateView):
	success_url = reverse_lazy('login')
	form_class = UserRegisterForm

	# Dealing with Post requests
	def post(self, request, *args, **kwargs):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			user.refresh_from_db()  # This brings the profile from db
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.gender = form.cleaned_data.get('gender')
			user.profile.country = form.cleaned_data.get('country')
			user.save()
			messages.success(
				request, f'Your account has been created! You are now able to log in!')
		return redirect('cardalog-home')


# Custom LoginView
class MyLoginView(SuccessMessageMixin, LoginView):
	success_url = reverse_lazy('cardalog-home')
	success_message = "Welcome back!"

	def post(self, request, *args, **kwargs):
		if request.is_ajax and request.method == "POST":
			login_form = AuthenticationForm(request, request.POST)

			if login_form.is_valid():
				username = login_form.cleaned_data['username']
				password = login_form.cleaned_data['password']
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					response_data = {'status': 'ok'}

			else:
				response_data = {'status': 'Form is not valid'}
		return response.HttpResponse(json.dumps(response_data), content_type='application/json')


# Custom PasswordResetView
class PasswordResetView(PasswordResetView):
	def post(self, request, *args, **kwargs):
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(email=data)
			for user in associated_users:
				subject = "Password Reset Requested"

				dic = {
					"email": user.email,
					'domain': '127.0.0.1:8000',
					'site_name': 'Cardalog',
					'uid': urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'user': user,
					'protocol': 'http',
				}
				rendered_email = render_to_string("password/password_reset_email.txt", dic)
				try:
					send_mail(subject, rendered_email, 'admin@example.com',[user.email], fail_silently=False)
				except BadHeaderError:
					return HttpResponse('Invalid header found.')
			return redirect('password_reset_done')		
		# If form was not valide, empty the form and reset the page	
		else:
			password_reset_form = PasswordResetForm()
			return render(request=request, template_name='password/password_reset.html', context={'form': password_reset_form})

# Custom PasswordResetDoneView
class PasswordResetDoneView(SuccessMessageMixin, PasswordResetDoneView):
	def get(self, request, *args, **kargs):
		messages.success(request, f'Email has been sent! See you there! :)')
		return redirect('cardalog-home')


# Custom PasswordResetCompleteView
class PasswordResetCompleteView(SuccessMessageMixin ,PasswordResetCompleteView):
	def get(self, request, *args, **kargs):
		messages.success(request, f'Your Password has been updated! Please login again! :D')
		return redirect('cardalog-home')

# Profile View (My Page)
@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		# Instance will tell which instance we are working on
		p_form = ProfileUpdateForm(
			request.POST, request.FILES, instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('cardalog-home')
	else:
		# Instance will bring current user data
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form,
	}

	return render(request, 'profile.html', context)