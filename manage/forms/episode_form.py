from django.forms import ModelForm
from ..models.episode import Episode
class EpisodeForm(ModelForm):
    class Meta:
        model = Episode
        exclude = [
            'bit_size',
            'episode_duration',
            'play_length',
            'show_fk',
            'file_type',
        ]