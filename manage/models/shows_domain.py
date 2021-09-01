import uuid
from django.db import models
from .show import Show
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

class ShowDomainsManager(models.Manager):
    def get_with_show_obj(self, show_obj):
        """
        Gets the Domain Object for a given Show Object.
        This is used to get the subdomain name for a given show.

        Input Arguements: show_obj must be a Show Object.
        Returns: A single Domain Object.
        """
        return self.get(show_fk=show_obj)

    def get_with_subdomain_name(self, subdomain):
        """
        Gets the Domain Object for a given subdomain.

        Input Arguements: pk_id must be a string
        Returns: A single Domain Object.
        """
        return self.get(show_website_name=subdomain)


class ShowDomains(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    show_website_name = models.CharField(unique=True, max_length=150)
    show_fk = models.OneToOneField(Show, on_delete=models.CASCADE, null=True, blank=True)

    objects = ShowDomainsManager()


@receiver(post_save, sender=Show)
def create_showdomain(sender, instance, created, **kwargs):
    if created:
        ShowDomains.objects.create(show_fk=instance, show_website_name=str(instance.id))