from django.db import models
from sets.models import Set

# Create your models here.
class Card(models.Model):
    term = models.CharField(max_length=100, blank=False)
    definition = models.CharField(max_length=150, blank=False)
    example = models.CharField(max_length=150, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    card_set = models.ForeignKey(Set, on_delete=models.CASCADE)

    def __str__(self):
        return self.term
    

    