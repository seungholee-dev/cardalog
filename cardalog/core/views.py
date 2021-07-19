from users.forms import UserRegisterForm
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['register_form'] = UserRegisterForm()
        return context