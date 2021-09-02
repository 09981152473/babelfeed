from django.shortcuts import render
from manage.models.show import Show
from manage.models.episode import Episode
from ..models.show_metrics import ShowMetrics
from ..models.episode_metrics import EpisodeMetrics


# Create your views here.
def show_metric(request, pk_id):
    """
    Retrieve and return the show and episode metrics for a given show.
    """
    show = Show.objects.get_show(pk_id)
    episodes = Episode.objects.get_episodes_for_show(show)

    show_metrics = ShowMetrics.objects.get_show_metric(show)
    # this should be all the metrics for all the shows
    # well need to sort this in a way to make sure that it's organized by date
    ep_metrics = EpisodeMetrics.objects.get_episodes_metrics(episodes)
    metric_dic = {}

    # Structuring the data so that we can easily use it with chart.js
    for ep in ep_metrics:
        key = ep.get_data_label()
        if key in metric_dic:
            metric_dic[key] += ep.download_count
        else:
            metric_dic[key] = ep.download_count

    labels = list(metric_dic.keys())
    data = list(metric_dic.values())

    print(labels)
    print(data)

    context = {
        "show": show,
        "episodes": episodes,
        "show_metrics": show_metrics,
        "ep_metrics": ep_metrics,
        "labels": labels,
        "data": data,
    }

    return render(request, "metrics_dashboard/index.html", context)


def episode_metric(request, sh_id, ep_id):
    """
    Retrieve and return the show and episode metrics for a given show.
    """
    show = Show.objects.get_show(sh_id)
    episodes = Episode.objects.get_episodes_for_show(show)

    show_metrics = ShowMetrics.objects.get_show_metric(show)
    ep_metrics = EpisodeMetrics.objects.get_episode_metrics_by_id(ep_id)

    labels = []
    data = []
    for ep in ep_metrics:
        labels.append(ep.get_data_label())
        data.append(ep.download_count)

    context = {
        "show": show,
        "episodes": episodes,
        "show_metrics": show_metrics,
        "ep_metrics": ep_metrics,
        "labels": labels,
        "data": data,
    }
    return render(request, "metrics_dashboard/index.html", context)
