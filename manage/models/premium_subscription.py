import uuid
from django.db import models
from .show import Show
from accounts.models.profile import Profile

class PremiumSubscriptionsManager(models.Manager):

    def get_users_subscriptions(self, user_profile):
        """
        Gets the subscriptions for a particular user.

        Input Arguments: user_profile must be a Profile Object
        Returns: A QuerySet that contains all Subscriptions for a particular user
        """
        return self.filter(profile_fk=user_profile)

    def unsubscribe(self, show, profile):
        """
        Delete a subscription.

        Input Arguments: Show must be an Show Object and Profile must be a Profile Object for the User.
        Returns: Nothing.
        """
        instance = self.get_subscription_for_show_for_user(show, profile)
        instance.delete()

    def get_premium_show(self, sub_id):
        """
        Gets the subscription object for a given key.

        Input Arguments: sub_id must be a UUID
        Returns: Nothing.
        """
        return self.get(id=sub_id)

    def get_subscription_for_show_for_user(self, show_id, profile):
        """
        Gets the Subscription object for user and a show.

        Input Arguments: show_id must be a Show Object, profile must be a Profile object for the User.
        Returns: A single subscription object.
        """
        return self.get(show_fk=show_id, profile_fk=profile)


class PremiumSubscriptions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    show_fk = models.ForeignKey(Show, related_name="premium_show", on_delete=models.CASCADE)
    profile_fk = models.ForeignKey(Profile, related_name="subscribed_user", on_delete=models.CASCADE)

    objects = PremiumSubscriptionsManager()

    def __str__(self):
        return str(self.profile_fk) + ": " + str(self.show_fk)