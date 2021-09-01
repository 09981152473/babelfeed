import uuid
from django.db import models
from babelcast import settings
from accounts.models.profile import Profile
from ..utils.enums import CategoryChoices, ExplictSetting, LanguageChoices, ShowType
from ..classes.filevalidator import validate_image_file
from manage.classes.customStorage import CustomStorage
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver


class ShowManager(models.Manager):

    def get_shows(self):
        """
        Gets a complete list of all Show Database Entries.

        Input Arguements: None
        Returns: A QuerySet of Show Objects
        """
        return self.all()

    def get_show(self, pk_id):
        """
        Gets the show object for a given key.

        Input Arguments: pk_id must be a UUID
        Returns: A single show object
        """
        return self.get(id=pk_id)

    def get_shows_by_profile(self, profile):
        """
        Gets the show object for a given profile.

        Input Arguements: profile must be a Profile object
        Returns: A QuerySet of Show Objects
        """
        return self.filter(profile_fk=profile)

    def delete_show(self, pk_id):
        """
        Deletes a Show Object given a key.

        Input Arguements: pk_id must be a UUID
        Returns: Delete single show object
        """
        self.get_show(pk_id).delete()


class Show(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    show_name = models.CharField(max_length=50)
    description = models.TextField()
    summary = models.CharField(max_length=50, default=0)
    language = models.CharField(max_length=150, choices=LanguageChoices.choices)
    author = models.CharField(max_length=50)
    copyright = models.CharField(max_length=50)

    def change_file_name(instance, filename):
        return instance.get_relative_image_url()

    # I'm putting blank = true so that edit form will work, we need to change the validation so that it can't be blank during creation, but can be blank during editing
    icon = models.ImageField(upload_to=change_file_name, null=True, validators=[validate_image_file])

    category = models.CharField(max_length=150, choices=CategoryChoices.choices)
    explict_rating = models.CharField(max_length=150, choices=ExplictSetting.choices)
    premium_feed = models.BooleanField(default=False)
    release_date = models.DateTimeField(auto_now=True)
    show_type = models.CharField(max_length=25, choices=ShowType.choices)
    profile_fk = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)

    contact_show_name = models.CharField(max_length=50, default="test owner")
    contact_show_email = models.CharField(max_length=50, default="testowner@gmail.com")
    facebook_username = models.CharField(max_length=32, blank=True, default="")
    twitter_username = models.CharField(max_length=32, blank=True, default="")
    instagram_username = models.CharField(max_length=32, blank=True, default="")
    tiktok_username = models.CharField(max_length=32, blank=True, default="")
    youtube_username = models.CharField(max_length=32, blank=True, default="")
    reddit_username = models.CharField(max_length=32, blank=True, default="")

    objects = ShowManager()

    def save(self, *args, **kwargs):
        try:
            this = Show.objects.get_episode(pk_id=self.id)
            if this.icon != self.icon:
                self.icon.name = this.icon.name
                s3 = CustomStorage()
                s3.delete_episode(this)
            else:
                print("Audio is the same")
        except: pass
        super(Show, self).save(*args, **kwargs)

    def __str__(self):
        return self.show_name

    def get_id_str(self):
        return str(self.id)

    def get_absolute_url(self):
        return "https://" + settings.AWS_STORAGE_BUCKET_NAME +'.s3.' + settings.AWS_S3_REGION_NAME + '.amazonaws.com/' + self.get_id_str() + '/'

    def image_file_path(self):
        return self.get_id_str() + ".png"

    def get_relative_image_url(self):
        """
        Relative url to the image stored on the backend
        """
        return self.get_id_str() + "/" + self.image_file_path()

    def get_absolute_image_url(self):
        """
        Direct url to the image stored on the backend.
        """
        return self.get_absolute_url() + self.image_file_path()

    # I think this is used
    # this might be fucked
    def generate_absolute_uri(self, request):
        return request.build_absolute_uri('/show/' + self.get_id_str())



@receiver(pre_delete, sender=Show)
def delete_show_hook(sender, instance, using, **kwargs):
    storage = CustomStorage()
    storage.delete_show(instance.get_id_str())


