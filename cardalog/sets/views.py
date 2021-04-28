from sets.models import Set
from cards.models import Card
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
class SetListView(ListView):
    model = Set
    template_name = "set_list.html"
    context_object_name = 'sets'

class SetDetailView(DetailView):
    model = Set
    template_name = "set_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_list'] = Card.objects.all()
        return context