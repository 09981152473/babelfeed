from json import dumps

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from manage.models.episode import Episode
from manage.models.show import Show
from manage.models.shows_domain import ShowDomains
from manage.models.premium_subscription import PremiumSubscriptions
from accounts.models.profile import Profile
from metrics_dashboard.models.show_metrics import ShowMetrics
from manage.utils.enums import CategoryChoices

def premium_show_view(request, pk_id):
    """
    Displays the landing page for a premium show that the logged in user is not subscribed too.

    Input: show_id should always be the id for the premium show.
    """
    context = {"id": pk_id}
    return render(request, "shows_frontend/premium_landing_page.html", context)


def subscribe_to_premium_feed_view(request, pk_id):
    """
    View to create a subscription to a premium show for a user.

    Input: Should always be the ID (UUID) for the show that we're subscribing too.
    """

    show = Show.objects.get_show(pk_id)
    profile = Profile.objects.get_profile(request.user)

    PremiumSubscriptions.objects.create(show_fk=show, profile_fk=profile)
    website_name = ShowDomains.objects.get_with_show_obj(show).show_website_name

    return HttpResponseRedirect(reverse("show_frontend", args=[website_name]))


def show_episode_frontend_view(request, pk_id, ep_id):
    """
    Placeholder.
    We need a view for individual episodes.
    This should have it's on JS player and just a single episode.
    Maybe we could also just have url that routes to the base frontend of th show and has the episode 'preselected' to play.
    """
    context = {"episode": Episode.objects.get_episode(ep_id)}
    return render(request, "shows_frontend/episode_frontend.html", context)


def show_frontend(request, pk_id):
    """
    Takes in a subdomain and retrieves the front-end info for the show.
    We check to see if the subdomain provided is valid and then if it's a premium show.
    Logged in users must be subscribed to the premium feed to veiw the front end of a premium show.
    A list of episodes is passed to the template so that the user can play the podcast with a JS player.
    """
    show = ShowDomains.objects.get_with_subdomain_name(pk_id).show_fk
    profile = Profile.objects.get_profile(request.user.id)
    if show.premium_feed:
        if request.user.is_authenticated:
            try:
                PremiumSubscriptions.objects.get_subscription_for_show_for_user(show, profile)
            except ObjectDoesNotExist:
                # The user is not subscribed to the premium show feed, we redriect to the landing page
                return premium_show_view(request, show.id)

    ep = Episode.objects.get_episodes_for_show(show)

    name = []
    ep_url = []
    duration = []

    for e in ep:
        name.append(e.name)
        ep_url.append(request.build_absolute_uri("/content/audio/" + str(show.id) + "/") +
                      e.get_audio_name())
        duration.append(e.get_length_as_str())

    name = dumps(name)
    ep_url = dumps(ep_url)
    duration = dumps(duration)

    show_metric = ShowMetrics.objects.get_show_metric(show)
    show_metric.increase_frontend_traffice()

    context = {"name": name, "url": ep_url, "duration": duration, "show": show, "index_audio": 0}
    print(context)
    return render(request, "shows_frontend/show_frontend.html", context)
