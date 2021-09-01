import uuid
import time
from django.db import models
from .show import Show
from manage.utils.enums import ExplictSetting, EpisodeTypes
from manage.classes.filevalidator import validate_image_file, validate_audio_file
from manage.classes.customStorage import CustomStorage
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils import timezone

class EpisodeManager(models.Manager):

    def get_episodes_for_show(self, show):
        """
        Gets the Episode Objects for a given show.

        Input Arguments: Show must be a Show Object.
        Returns: A QuerySet of Episode Objects.
        """
        return self.filter(show_fk=show)

    def get_future_episodes_for_Show(self, show_obj, include_unpublished=False):
        """
        Gets all Episode Objects for a given show that haven't been released yet.

        Input Arguments: Show must be a Show Object. include_unpublished should be a boolean.
        Returns: A QuerySet of Episode Objects.
        """
        curr_date = timezone.now()
        if include_unpublished:
            return self.get_episodes_for_show(show_obj).filter(release_date__gte=curr_date).order_by("release_date")
        else:
            return self.get_episodes_for_show(show_obj).filter(release_date__gte=curr_date, published=True).order_by("release_date")


    def get_released_episodes_for_show(self, show_obj, include_unpublished=False):
        """
        Gets all Episode Objects for a given show that have been released.

        Input Arguments: Show must be a Show Object. include_unpublished should be a boolean.
        Returns: A QuerySet of Episode Objects.
        """
        curr_date = timezone.now()
        if include_unpublished:
            return self.get_episodes_for_show(show_obj).filter(release_date__lte=curr_date).order_by("release_date")
        else:
            return self.get_episodes_for_show(show_obj).filter(release_date__lte=curr_date, published=True).order_by("release_date")

    def get_episode(self, pk_id):
        """
        Gets the Episode Object for a given key.

        Input Arguments: pk_id must be a UUID
        Returns: A single Episode Object.
        """
        return self.get(id=pk_id)

    def delete_episode(self, pk_id):
        """
        Gets the Episode Object for a given key.

        Input Arguments: pk_id must be a UUID
        Returns: A single Episode Object.
        """
        self.get_episode(pk_id).delete()


class Episode(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    show_fk = models.ForeignKey(Show, related_name="episode_id", on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    description = models.TextField()
    summary = models.CharField(max_length=50, default=0)
    bit_size = models.CharField(max_length=50)
    play_length = models.CharField(max_length=50, default=0)
    explict_rating = models.CharField(max_length=150, choices=ExplictSetting.choices)
    episode_type = models.CharField(max_length=25, choices=EpisodeTypes.choices)
    season_number = models.IntegerField(default=0)
    episode_number = models.IntegerField(default=0)
    file_type = models.CharField(max_length=50)
    release_date = models.DateTimeField(default=timezone.now)
    published = models.BooleanField(default=False)

    def change_ep_image(instance, filename):
        return instance.get_episode_image_path()
    icon = models.ImageField(upload_to=change_ep_image, blank=True, null=True, validators=[validate_image_file])

    def change_ep_audio(instance, filename):
        return instance.get_episode_audio_path()
    audio = models.FileField(upload_to=change_ep_audio, null=True, validators=[validate_audio_file])

    objects = EpisodeManager()

    def save(self, *args, **kwargs):
        try:
            this = Episode.objects.get_episode(pk_id=self.id)
            if this.audio != self.audio:
                self.audio.name = this.audio.name
                s3 = CustomStorage()
                s3.delete_episode(this)
            else:
                print("Audio is the same")
        except: pass
        super(Episode, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_id_str(self):
        return str(self.id)

    def get_length_as_str(self):
        sec = int(self.play_length)
        ty_res = time.gmtime(sec)
        res = time.strftime("%H:%M:%S", ty_res)
        return res

    def get_audio_name(self):
        return self.get_id_str() + ".mp3"

    def get_episode_img_path(self):
        return self.get_id_str() + ".png"

    def get_episode_image_path(self):
        return self.show_fk.get_id_str() + "/" +  self.get_episode_img_path()

    def get_episode_audio_path(self):
        return self.show_fk.get_id_str() + "/" + self.get_audio_name()

    def content_path_to_audio(self):
        """
        This is used to grab the address of the episode's audio file in our S3 bucket.
        """
        if self.icon:
            return self.show_fk.get_absolute_url() + self.get_audio_name()


    def content_path_to_img(self):
        """
        This is used to grab the address of the episode's image file in our S3 bucket.
        """
        return self.show_fk.get_absolute_url() + self.get_episode_img_path()

@receiver(pre_delete, sender=Show)
def delete_episode_hook(sender, instance, using, **kwargs):
    storage = CustomStorage()
    storage.delete_episode(instance)
