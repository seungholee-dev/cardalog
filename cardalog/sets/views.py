from sets.models import Set
from cards.models import Card
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
class SetListView(ListView):
    model = Set
    template_name = "set_list.html"
    context_object_name = 'sets'

class SetDetailView(DetailView):
    model = Set
    template_name = "set_detail.html"

class SetCreateView(CreateView):
    model = Set
    template_name = "set_create.html"
    success_url = '/sets/list/' # Where to direct once the form is valid
    fields = ['title', 'description', 'category', 'is_public']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)