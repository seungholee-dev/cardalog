from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Set(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=30, blank=False)
    description = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=30, blank=False)
    is_public = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)