from manage.models.show import Show
from manage.models.episode import Episode
from metrics_dashboard.models.show_metrics import ShowMetrics
from metrics_dashboard.models.episode_metrics import EpisodeMetrics
from django.shortcuts import redirect

# These view manage the path to audio and image files on AWS
# The RSS feed uses these views so that we can track audience traffic and episode download metrics
def audio_view(request, show_id, audio_id):
     ep = Episode.objects.get_episode(audio_id)
     url = ep.content_path_to_audio()

     EpisodeMetrics.objects.increment_metric(ep)
     ShowMetrics.objects.increment_download_count(ep.show_fk)

     return redirect(url)


def show_image_view(request, show_id, img_id):
     show = Show.objects.get_show(show_id)
     url = show.get_show_image_url()
     print(url)
     return redirect(url)