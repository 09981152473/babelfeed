from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from manage.models.show import Show
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class ShowMetricsManager(models.Manager):

    def get_show_metric(self, show_db_obj):
        return self.get(show_fk=show_db_obj)

    def increment_download_count(self, show_db_obj):
        metric = self.get_show_metric(show_db_obj)
        metric.download_count += 1


class ShowMetrics(models.Model):
    show_fk = models.OneToOneField(Show, on_delete=models.CASCADE)
    download_count = models.IntegerField(default=0)

    frontend_traffic = models.IntegerField(default=0)

    facebook_redirect_count = models.IntegerField(default=0)
    twitter_redirect_count = models.IntegerField(default=0)
    instagram_redirect_count = models.IntegerField(default=0)
    tiktok_redirect_count = models.IntegerField(default=0)
    youtube_redirect_count = models.IntegerField(default=0)
    reddit_redirect_count = models.IntegerField(default=0)

    objects = ShowMetricsManager()

    def increase_download_count(self):
        self.download_count += 1

    def increase_frontend_traffice(self):
        self.frontend_traffic += 1

    def increase_facebook_count(self):
        self.facebook_redirect_count += 1

    def increase_twitter_count(self):
        self.twitter_redirect_count += 1

    def increase_instagram_count(self):
        self.instagram_redirect_count += 1

    def increase_tiktok_count(self):
        self.tiktok_redirect_count += 1

    def increase_youtube_count(self):
        self.youtube_redirect_count += 1

    def increase_reddit_count(self):
        self.reddit_redirect_count += 1

@receiver(post_save, sender=Show)
def create_show_metrics(sender, instance, created, **kwargs):
    if created:
        ShowMetrics.objects.create(show_fk=instance)


@receiver(post_save, sender=Show)
def save_show_metrics(sender, instance, **kwargs):
    instance.showmetrics.save()
