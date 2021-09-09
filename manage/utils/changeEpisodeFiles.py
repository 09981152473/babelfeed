"""
Instance should be an episode object.
Note, there's probably a better way to do this.
Maybe just have it in the episode.py file with the model class
"""

def change_ep_audio(instance, filename):
    return instance.get_episode_audio_path()


def change_ep_image(instance, filename):

    return instance.get_episode_image_path()