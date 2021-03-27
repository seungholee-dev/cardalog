from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(SuccessMessageMixin, CreateView):
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')
	form_class = UserRegisterForm
	success_message = "Your profile was created successfully"

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

		return redirect('login')
