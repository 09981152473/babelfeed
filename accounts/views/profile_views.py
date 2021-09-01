from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from ..models.profile import Profile
from manage.models.show import Show
from ..form.profile_form import ProfileForm
from manage.models.premium_subscription import PremiumSubscriptions
from manage.models.show import Show
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/accounts/login/')
def user_profile(request):
    """
    Returns logged in User's profile.
    """

    profile = Profile.get_logged_in_profile(request)
    context = (Show.objects.get_shows_by_profile(profile))
    return render(request, "manage/profile_page.html", {"shows": context})


@login_required(login_url='/accounts/login/')
def update_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        model = form.save(commit=False)
        model.user_fk = request.user
        model.save()
        return render(request, 'manage/edit_profile.html', {'form': form})

    else:
        logged_in_profile = Profile.get_logged_in_profile(request)
        form = ProfileForm(instance=logged_in_profile)
        return render(request, 'manage/edit_profile.html', {'form': form})


@login_required(login_url='/accounts/login/')
def premium_feed_list(request):
    profile = Profile.objects.get_profile(request.user)
    try:
        feed_list = PremiumSubscriptions.objects.get_users_subscriptions(profile)
        context = {"premium_feed": feed_list}
        return render(request, 'manage/manage_premium_feeds.html', context)

    except:
        # We should
        return render(request, 'manage/manage_premium_feeds.html')

@login_required(login_url='/accounts/login/')
def unsubscribe_from_premium_feed(request, pk_id):
    profile = Profile.objects.get_profile(request.user)
    show = Show.objects.get_show(pk_id)
    PremiumSubscriptions.objects.unsubscribe(show, profile)

    return HttpResponseRedirect(reverse("subscriptions"))