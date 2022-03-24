from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, Profile


@receiver(post_save, sender=User)
def userCreated(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
        )


@receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **Kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.username = profile.username
        user.first_name = profile.name
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def profileDeleted(sender, instance, **kwargs):
    user = instance.user
    user.delete()
