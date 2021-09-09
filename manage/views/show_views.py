from accounts.models.profile import Profile
from django.shortcuts import redirect, render
from manage.models.show import Show
from manage.models.episode import Episode
from manage.models.shows_domain import ShowDomains
from manage.classes.customStorage import CustomStorage
from ..forms.show_from import ShowForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView


@login_required(login_url='/accounts/login/')
def create_show(request):
    if request.method == "POST":
        form = ShowForm(request.POST, request.FILES)
        if form.is_valid():

            show_m = form.save(commit=False)
            show_m.profile_fk = Profile.get_logged_in_profile(request)
            show_m.save()

            return redirect('user_profile')
        else:
            print("Form isn't valid.")
    else:
        form = ShowForm()
    return render(request, 'manage/create_show.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ShowDBUpdateView(UpdateView):
    model = Show
    fields = '__all__'
    template_name = 'manage/update_show.html'

    def get_success_url(self, **kwargs):
        return "../show_detail/" + str(self.object.id)


@login_required(login_url='/accounts/login/')
def show_detail(request, pk_id):
    show_context = Show.objects.get_show(pk_id)
    episode_context = Episode.objects.get_episodes_for_show(show_context)
    website = ShowDomains.objects.get_with_show_obj(show_context)

    edit_show_url = request.build_absolute_uri('/manage/edit_show/' + str(website.id) + "/website")
    #show_url = request.build_absolute_uri('../../show/' + str(website.show_website_name))
    domain = request.META['HTTP_HOST']
    if "www." in domain:
        show_url = "http://www." + str(website.show_website_name) + ".babelfeed.com"
    else:
        #pass
        show_url = "http://" +str(website.show_website_name) + ".localhost:8000"

    context = {
        "show": show_context,
        "episode": episode_context,
        "edit_show_site": edit_show_url,
        "show_site": show_url,
    }

    return render(request, "manage/show_detail.html", context)


@login_required(login_url='/accounts/login/')
def delete_show_view(request, pk_id):
    show_context = Show.objects.get_show(pk_id)
    owner_id = show_context.profile_fk.user_fk.id
    logged_id = request.user.id

    if owner_id is not logged_id:
        return redirect('access_denied')

    media_storage = CustomStorage()
    media_storage.delete_show(show_context.get_id_str())
    show_context.delete()
    return redirect('user_profile')
