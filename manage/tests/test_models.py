from django.test import TestCase, Client
from ..models.premium_subscription import PremiumSubscriptions
from ..models.show import Show
from ..models.episode import Episode
from accounts.models.profile import Profile
from accounts.form.profile_form import ProfileForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from ..forms.show_domain_form import ShowDomainsForm
from ..forms.episode_form import EpisodeForm
from ..forms.show_from import ShowForm
from django.utils.timezone import timedelta, datetime


# Create your tests here.
class ShowTest(TestCase):
    test_show_id = ""

    def setUp(self):
        show = Show.objects.create(show_name="Test Show")
        self.test_show_id = show.id

    def test_show_was_created(self):
        show = Show.objects.get_show(self.test_show_id)
        self.assertIsNot(show, None)

    def test_show_by_profile(self):
        show = Show.objects.get_show(self.test_show_id)
        user_id = User.objects.create(username="Test User").id
        p = Profile.objects.get_profile(user_id)
        show.profile_fk = p
        show.save()
        qs = Show.objects.get_shows_by_profile(p)
        self.assertEqual(qs.count(), 1)

    def test_get_shows(self):
        Show.objects.create(show_name="Test Show 2")
        Show.objects.create(show_name="Test Show 3")
        Show.objects.create(show_name="Test Show 4")

        qs = Show.objects.get_shows()

        self.assertEqual(qs.count(), 4)


    def test_cleanup_show(self):
        Show.objects.delete_show(self.test_show_id)
        self.assertRaises(ObjectDoesNotExist, Show.objects.get_show, self.test_show_id)

    def test_empty_form(self):
        form = ShowForm()
        self.assertIn("show_name", form.fields)
        self.assertIn("description", form.fields)
        self.assertNotIn("profile_fk", form.fields)


class EpisodeTest(TestCase):
    test_episode_id = None
    test_show_id = None

    def setUp(self):
        show = Show.objects.create(show_name="Test Show")
        self.test_show_id = show.id
        self.test_episode_id = Episode.objects.create(episode_name="Test Show", show_fk=show, published=True).id

        Episode.objects.create(episode_name="Test Show", show_fk=show, published=True)
        future_ep = Episode.objects.create(episode_name="Test Show", show_fk=show, published=True)
        future_ep.release_date = future_ep.release_date + timedelta(hours=14)
        future_ep.save()

        Episode.objects.create(episode_name="Test Show 2", show_fk=show, published=True)
        Episode.objects.create(episode_name="Test Show 2", show_fk=show, published=False)

    def test_get_episode_list(self):
        qs = Episode.objects.get_episodes_for_show(self.test_show_id)
        self.assertEqual(qs.count(), 5)

    def test_episode_creation(self):
        show = Episode.objects.get_episode(self.test_episode_id)
        self.assertIsNot(show, None)

    def test_released_episodes(self):
        # published and released date has passed
        qs = Episode.objects.get_released_episodes_for_show(self.test_show_id)
        self.assertEqual(qs.count(), 3)

        # unpublished and released date has passed
        qs = Episode.objects.get_released_episodes_for_show(self.test_show_id, include_unpublished=True)
        self.assertEqual(qs.count(), 4)

        # unreleased
        qs = Episode.objects.get_future_episodes_for_Show(self.test_show_id)
        self.assertEqual(qs.count(), 1)


    def test_empty_form(self):
        form = EpisodeForm()
        self.assertIn("episode_name", form.fields)
        self.assertIn("description", form.fields)
        self.assertNotIn("bit_size", form.fields)
        self.assertNotIn("episode_duration", form.fields)
        self.assertNotIn("play_length", form.fields)
        self.assertNotIn("show_fk", form.fields)
        self.assertNotIn("file_type", form.fields)


class ProfileTest(TestCase):
    user_id = None

    def setUp(self):
        self.user_id = User.objects.create(username="Test User").id

    def test_profile_creation(self):
        profile_qs = Profile.objects.get_profile(self.user_id)
        user = User.objects.get(id=self.user_id)

        self.assertEqual(profile_qs.user_fk, user)

    def test_empty_form(self):
        form = ProfileForm()
        self.assertIn("contact_name", form.fields)
        self.assertIn("contact_email", form.fields)
        self.assertNotIn("user_fk", form.fields)


class ShowDomainTest(TestCase):

    def setUp(self):
        pass

    def test_empty_form(self):
        form = ShowDomainsForm()
        self.assertIn("show_website_name", form.fields)
        self.assertIn("show_fk", form.fields)


class PremiumSubscriptionTest(TestCase):
    user = None
    show = None

    def setUp(self):
        temp = User.objects.create(username="Test User")
        self.user = Profile.objects.get_profile(temp)
        self.show = Show.objects.create(show_name="Test Show")
        PremiumSubscriptions.objects.create(show_fk=self.show, profile_fk=self.user)

    def test_premiumsub_creation(self):
        sub = PremiumSubscriptions.objects.get_subscription_for_show_for_user(self.show, self.user)
        self.assertEqual(sub.show_fk, self.show)
        self.assertEqual(sub.profile_fk, self.user)

    def test_unsubscribe(self):
        PremiumSubscriptions.objects.unsubscribe(self.show, self.user)

        self.assertRaises(ObjectDoesNotExist,
                          PremiumSubscriptions.objects.get_subscription_for_show_for_user, self.show, self.user)
