from django.forms import ModelForm
from ..models.shows_domain import ShowDomains

class ShowDomainsForm(ModelForm):
    class Meta:
        model = ShowDomains
        exclude = ['show_fk']