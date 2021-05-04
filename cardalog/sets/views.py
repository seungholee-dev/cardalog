from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from sets.models import Set
from cards.models import Card
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

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
    success_url = reverse_lazy('set-list') # Where to direct once the form is valid
    fields = ['title', 'description', 'category', 'is_public']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class SetDeleteView(DeleteView):
    model = Set
    success_url = reverse_lazy('set-list')

class SetUpdateView(SuccessMessageMixin, UpdateView):
    model = Set
    template_name = "set_update.html"
    fields = ['title', 'description', 'category', 'is_public']
    success_message = "Your set has been updated!"
    
    # Redirect User to the updated set DetailView
    def get_success_url(self):
        return reverse_lazy('set-detail', kwargs={"pk": self.object.id})