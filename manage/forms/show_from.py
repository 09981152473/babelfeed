from django.forms import ModelForm
from ..models.show import Show


class ShowForm(ModelForm):
    class Meta:
        model = Show
        exclude = [
            'profile_fk',
            'release_date',
         ]