from django.db.models.signals import post_save
from django.dispatch import receiver
from .models.profile import Profile
from .models.customer import Customer

@receiver(post_save, sender=Customer)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(customer=instance)

@receiver(post_save, sender=Customer)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()