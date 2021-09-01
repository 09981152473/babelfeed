from django.test import TestCase
from ..models.episode_metrics import EpisodeMetrics
from ..models.show_metrics import ShowMetrics
from manage.models.show import Show
from manage.models.episode import Episode
from django.utils.timezone import timedelta, datetime


# Create your tests here.
class ShowMetricsTest(TestCase):
    test_show_id = ""

    def setUp(self):
        test_show_id = Show.objects.create(show_name="Test Show").id

    # Tests that show metrics are created when shows are created
    def test_show_metric_creation(self):
        show = Show.objects.get(show_name="Test Show")
        test_metric = ShowMetrics.objects.get_show_metric(show)
        self.assertNotEqual(test_metric, None)

    # Test social media
    def test_social_media_tracking(self):
        show = Show.objects.get(show_name="Test Show")
        test_metric = ShowMetrics.objects.get_show_metric(show)

        test_metric.increase_facebook_count()
        test_metric.increase_twitter_count()
        test_metric.increase_instagram_count()
        test_metric.increase_tiktok_count()
        test_metric.increase_youtube_count()
        test_metric.increase_reddit_count()

        self.assertEqual(test_metric.facebook_redirect_count, 1)
        self.assertEqual(test_metric.twitter_redirect_count, 1)
        self.assertEqual(test_metric.instagram_redirect_count, 1)
        self.assertEqual(test_metric.tiktok_redirect_count, 1)
        self.assertEqual(test_metric.youtube_redirect_count, 1)
        self.assertEqual(test_metric.reddit_redirect_count, 1)

    def test_download_count(self):
        show = Show.objects.get(show_name="Test Show")
        test_metric = ShowMetrics.objects.get_show_metric(show)

        test_metric.increase_download_count()

        self.assertEqual(test_metric.download_count, 1)

    def test_metric_cleanup(self):
        Show.objects.delete_show(self.test_show_id)
        pass


class EpisodeMetricsTest(TestCase):
    test_ep_id = ""

    def setUp(self):
        test_show = Show.objects.create(show_name="Test Show")
        test_ep = Episode.objects.create(episode_name="Test Episode", show_id=test_show)
        self.test_ep_id = test_ep.id

    # Tests that show metrics are created when shows are created
    def test_episode_creation(self):
        test_episode = Episode.objects.get_episode(self.test_ep_id)
        test_metrics = EpisodeMetrics.objects.get_episodes_metrics(test_episode)

        self.assertNotEqual(test_metrics, None)

    def test_download_count(self):
        test_episode = Episode.objects.get_episode(self.test_ep_id)
        test_metrics = EpisodeMetrics.objects.get_episodes_metrics(test_episode)[0]

        test_metrics.increase_download_count()

        self.assertEqual(test_metrics.download_count, 1)

    # Tests to ensure that a new metric object is created when the date threshold is reached
    def test_increment_and_creation(self):
        test_episode = Episode.objects.get_episode(self.test_ep_id)
        test_metrics = EpisodeMetrics.objects.get_episodes_metrics(test_episode)[0]
        test_metrics.start_date = test_metrics.start_date - timedelta(hours=1)
        test_metrics.end_date = test_metrics.end_date - timedelta(hours=1)
        test_metrics.save()

        EpisodeMetrics.objects.increment_metric(test_episode)

        new_queryset = EpisodeMetrics.objects.get_episodes_metrics(test_episode)

        self.assertEqual(new_queryset.count(), 2)

    # Ensure that the episode metrics are deleted when the episode is delete
    def test_metric_cleanup(self):
        Episode.objects.delete_episode(self.test_ep_id)
        test_metrics = EpisodeMetrics.objects.get_episode_metrics_by_id(self.test_ep_id)

        self.assertNotEqual(test_metrics, None)

