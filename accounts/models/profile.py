from django.db import models
import uuid
from django.contrib.auth.models import User


class ProfileManager(models.Manager):

    def get_profile(self, user_id):
        """
        Gets the Profile Object for a given user.

        Input Arguments: user_id must be a User object.
        Returns: A single Profile Object.
        """
        return self.get(user_fk=user_id)


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user_fk = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=50, default="")
    contact_email = models.CharField(max_length=50, default="")

    objects = ProfileManager()

    def __str__(self):
        return self.user_fk.username

    def get_logged_in_profile(request):
        return Profile.get_profile(request.user)

    def get_profile(pk):
        return Profile.objects.get_profile(pk)


from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

# Create a profile when a user is registered and associate the newly created objects.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user_fk=instance)