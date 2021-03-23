from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Profile Model
class Profile(models.Model):
    BASIC = 1
    PREMIUM = 2
    PLAN = (
        (BASIC, "Basic"),
        (PREMIUM, "PREMIUM")
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(default='South Korea', max_length=30, blank=False)
    plan = models.PositiveSmallIntegerField(default=1, choices=PLAN, null=False, blank=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()