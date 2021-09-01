from django.urls import path
from .views import metrics_views

urlpatterns = [
    path('<uuid:pk_id>', metrics_views.show_metric, name="show_metric"),
    path('<uuid:sh_id>/<uuid:ep_id>', metrics_views.episode_metric, name="episode_metrics"),
]