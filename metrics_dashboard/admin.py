from django.contrib import admin
from .models.episode_metrics import EpisodeMetrics
from .models.show_metrics import ShowMetrics
# Register your models here.
admin.site.register(ShowMetrics)
admin.site.register(EpisodeMetrics)
