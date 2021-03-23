from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm
  success_message = "Your profile was created successfully"
