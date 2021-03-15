from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    BASIC = 1
    PREMIUM = 2
    PLAN = (
        (BASIC, "Basic"),
        (PREMIUM, "PREMIUM")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=30, blank=False)
    plan = models.PositiveSmallIntegerField(choices=PLAN, null=False, blank=False)

    def __str__(self):
        return self.user.username