from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserInteraction, Puzzle


@receiver(post_save, sender=Puzzle)
def track_user_interaction(sender, instance, created, **kwargs):
    if created:
        UserInteraction.objects.create(user=instance.user, puzzle=instance)
