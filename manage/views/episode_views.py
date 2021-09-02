import mutagen
from django.shortcuts import redirect, render
from manage.classes.customStorage import CustomStorage
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from manage.models.show import Show
from manage.models.episode import Episode
from manage.forms.episode_form import EpisodeForm
from accounts.models.profile import Profile
from django.http import HttpResponseRedirect
from django.urls import reverse

def does_profile_match_show(request, show_id):
    show_model = Show.objects.get_show(show_id)
    logged_in_profile = Profile.get_logged_in_profile(request)
    match = str(show_model.profile_fk.id) != str(logged_in_profile.id)

    result = {
        "show": show_model,
        "profile": logged_in_profile,
        "matched": match,
    }

    return result


@login_required(login_url='/accounts/login/')
def create_episode(request, pk_id):
    results = does_profile_match_show(request, pk_id)

    if results['matched']:
        print("Access Denied")
        return redirect('access_denied')

    if request.method == "POST":
        form = EpisodeForm(request.POST, request.FILES)
        if form.is_valid():

            ep_model = form.save(commit=False)
            show_model = results['show']

            ep_model.process_ep_upload_data(request, show_model)


            #audio_info = mutagen.File(ep_model.audio).info

            #file_obj = request.FILES['audio']
            #file_size = file_obj.size
            #ep_model.play_length = str(int(audio_info.length))
            #ep_model.show_fk = show_model
            #ep_model.bit_size = file_size
            #ep_model.file_type = "audio/mpeg"

            ep_model.save()

            return redirect('user_profile')
    else:
        form = EpisodeForm()
    return render(request, 'manage/create_episode.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class EpisodeUpdateView(UpdateView):
    model = Episode
    fields = '__all__'
    template_name = 'manage/update_episode.html'

    def get_success_url(self, **kwargs):
        return "../episode_detail/" + str(self.object.id)


@login_required(login_url='/accounts/login/')
def episode_detail(request, pk_id):
    context = {"episode": Episode.objects.get_episode(pk_id)}
    return render(request, "manage/episode_details.html", context)


@login_required(login_url='/accounts/login/')
def delete_episode_view(request, pk_id):
    ep = Episode.objects.get_episode(pk_id)

    owner_id = ep.show_fk.profile_fk.user_fk.id
    logged_id = request.user.id

    if owner_id is not logged_id:
        return redirect('access_denied')

    media_storage = CustomStorage()
    media_storage.delete_episode(ep)

    ep.delete()
    return HttpResponseRedirect(reverse("show_detail", args=[ep.show_fk.id]))