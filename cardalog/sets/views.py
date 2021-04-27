from sets.models import Set
from django.views.generic.list import ListView

# Create your views here.
class SetListView(ListView):
    model = Set
    template_name = "set_list.html"
    context_object_name = 'sets'