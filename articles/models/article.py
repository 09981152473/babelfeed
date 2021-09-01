from django.db import models

# Create your models here.
class Article(models.Model):
    body_text = models.CharField(max_length=2500, null=True)