from django.shortcuts import redirect
from manage.models.show import Show
from metrics_dashboard.models.show_metrics import ShowMetrics

def facebook_link_view(request, pk_id):
    show = Show.objects.get_show(pk_id)
    fb = show.facebook_username
    url = "https://www.facebook.com/" + fb

    metrics = ShowMetrics.objects.get_show_metric(show)
    metrics.increase_facebook_count()
    metrics.save()

    return redirect(url)


def twitter_link_view(request, pk_id):
    show = Show.objects.get_show(pk_id)
    fb = show.twitter_username
    url = "https://www.twitter.com/" + fb

    metrics = ShowMetrics.objects.get_show_metric(show)
    metrics.increase_twitter_count()
    metrics.save()

    return redirect(url)


def instagram_link_view(request, pk_id):
    show = Show.objects.get_show(pk_id)
    fb = show.instagram_username
    url = "https://www.instagram.com/" + fb

    metrics = ShowMetrics.objects.get_show_metric(show)
    metrics.increase_instagram_count()
    metrics.save()

    return redirect(url)


def tiktok_link_view(request, pk_id):
    show = Show.objects.get_show(pk_id)
    fb = show.tiktok_username
    url = "https://www.tiktok.com/@" + fb

    metrics = ShowMetrics.objects.get_show_metric(show)
    metrics.increase_tiktok_count()
    metrics.save()

    return redirect(url)


def youtube_link_view(request, pk_id):
    show = Show.objects.get_show(pk_id)
    fb = show.youtube_username
    url = "https://www.youtube.com/channel/" + fb

    metrics = ShowMetrics.objects.get_show_metric(show)
    metrics.increase_youtube_count()
    metrics.save()

    return redirect(url)


def reddit_link_view(request, pk_id):
    show = Show.objects.get_show(pk_id)
    fb = show.reddit_username
    url = "https://www.reddit.com/r/" + fb

    metrics = ShowMetrics.objects.get_show_metric(show)
    metrics.increase_reddit_count()
    metrics.save()

    return redirect(url)
