from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
	form_class = UserRegisterForm
	success_message = "Your profile was created successfully"

	# Dealing with Post requests
	def post(self, request, *args, **kwargs):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.birth_date = form.cleaned_data.get('birth_date')
			user.profile.gender = form.cleaned_data.get('gender')
			user.profile.country = form.cleaned_data.get('country')
			user.save()
			messages.success(request, f'Your account has been created! You are now able to log in!')

		return redirect('login')