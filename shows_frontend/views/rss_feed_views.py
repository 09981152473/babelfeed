from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from manage.models.episode import Episode
from manage.models.show import Show
from manage.models.shows_domain import ShowDomains
from manage.models.premium_subscription import PremiumSubscriptions
from manage.utils.enums import CategoryChoices

def build_feed_context(request, show_obj):
    """
    A helper function to build a context object for the RSS feed views.
    Maybe move to a utils file?

    Input:  Should always be a Show Object that you want a feed for.
    Output: A dict object that contains the data needed to build the RSS feed.
    """
    show_category = show_obj.category
    main_cate = CategoryChoices.get_main_category(show_category)
    base_uri = request.build_absolute_uri("/content/")
    website_name = ShowDomains.objects.get_with_show_obj(show_obj).show_website_name
    print(website_name)
    base_episode_url = request.build_absolute_uri("/content/audio/" + str(show_obj.id) + "/")
    show_frontend = request.build_absolute_uri("/show/" + website_name)
    base_show_url = request.build_absolute_uri(show_frontend + "/")
    context = {
        "show": show_obj,
        "episodes": Episode.objects.get_released_episodes_for_show(show_obj),
        "show_frontend": show_frontend,
        "show_url": base_show_url,
        "main_category": main_cate,
        "sub_category": show_category,
        "base_uri": base_uri,
        "base_episode_url": base_episode_url,
    }

    return context


def premium_feed(request, auth_key):
    """
    Authenticate the user's access to a premium feed.
    If the user is authorized to use the feed, the feed is generated through the "show_feed" method that is used
    for standard feeds.

    Input: The id for the show that we want a feed for.
    """
    try:
        premium_sub = PremiumSubscriptions.objects.get_premium_show(auth_key)
        show_obj = Show.objects.get_show(premium_sub.show_fk)

        context = build_feed_context(request, show_obj)
        return render(request, 'shows_frontend/show_feed.xml', context, content_type='text/xml')
    except ObjectDoesNotExist:
        return render(request, 'access_denied.html')


def show_feed(request, pk_id):
    """
    Builds the RSS feed for the podcasts.
    If the podcast is a premium show, we return an 'access denied' page.

    Input: The id for the show that we want a feed for.
    """
    show_obj = Show.objects.get_show(pk_id)

    if show_obj.premium_feed:
        return render(request, 'access_denied.html')

    context = build_feed_context(request, show_obj)

    return render(request, 'shows_frontend/show_feed.xml', context, content_type='text/xml')

