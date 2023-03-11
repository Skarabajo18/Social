from django.db.models.signals import post_save
from .models import (
	UserAccount, UserProfile
)
from django.dispatch import receiver


@receiver(post_save, sender = UserAccount)
def create_profile(sender, instance, created, **kwargs):
	if created:
		UserProfile.objects.create(User=instance)