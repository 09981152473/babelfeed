from manage.models.shows_domain import ShowDomains
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView


@method_decorator(login_required, name='dispatch')
class ShowDomainsUpdateView(UpdateView):
    model = ShowDomains
    fields = '__all__'
    template_name = 'manage/update_website.html'

    def get_success_url(self, **kwargs):
        return "../../show_detail/" + str(self.object.show_fk.id)