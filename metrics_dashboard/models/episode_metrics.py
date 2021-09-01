from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from manage.models.episode import Episode
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.timezone import timedelta, datetime
from django.utils import timezone
import pytz


class EpisodeMetricsManager(models.Manager):

    def get_episodes_metrics(self, episode_db_obj):
        return self.filter(episode_fk__in=episode_db_obj).order_by('start_date')

    def get_episode_metrics_by_id(self, ep_id):
        return self.filter(episode_fk__id=ep_id).order_by('start_date')

    def increment_metric(self, episode_db_obj):
        """
        Increments the download counter for a given Episode Metric.
        A new metric is created if the download happens during a new hour long block.
        """
        curr_date = timezone.now()

        try:
            qs = self.get(
                episode_fk=episode_db_obj,
                start_date__lte=curr_date,
                end_date__gte=curr_date
            )
            qs.increase_download_count()
        except ObjectDoesNotExist:
            self.create(episode_fk=episode_db_obj)

class EpisodeMetrics(models.Model):
    episode_fk = models.ForeignKey(Episode, on_delete=models.CASCADE)
    download_count = models.IntegerField(default=0)

    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    objects = EpisodeMetricsManager()

    def __str__(self):
        s = str(self.episode_fk.show_fk)
        s += " - "
        s += str(self.episode_fk)
        s += " ( " + self.start_date.strftime('%A %d-%m-%Y, %H') + ":00 - " + \
             self.end_date.strftime('%A %d-%m-%Y, %H') + ":00 )"

        return s

    def get_data_label(self):
        return self.start_date.strftime('%d-%m-%Y, %H') + ":00"

    def increase_download_count(self):
        self.download_count += 1
        self.save()

@receiver(post_save, sender=EpisodeMetrics)
def init_date_bounds(sender, instance, created, **kwargs):
    if created:
        date = timezone.now()

        year = date.year
        month = date.month
        day = date.day
        hour = date.hour

        instance.start_date = datetime(year, month, day, hour, tzinfo=pytz.utc)
        instance.end_date = instance.start_date + timedelta(hours=1)

        instance.save()


@receiver(post_save, sender=Episode)
def create_episode_metrics(sender, instance, created, **kwargs):
    if created:
        ep = EpisodeMetrics.objects.create(episode_fk=instance)