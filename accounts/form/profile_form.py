from django.forms import ModelForm
from ..models.profile import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = [
            'user_fk'
        ]