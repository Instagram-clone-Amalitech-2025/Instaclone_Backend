from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new profile if the user was just created
        Profile.objects.create(user=instance)
    else:
        # Save the profile for existing users
        instance.profile.save()
