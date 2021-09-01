from django.urls import path
from . import views
from .views import show_views, show_domain_views, episode_views
from accounts.views import profile_views
from .views import *
urlpatterns = [
    path('', profile_views.user_profile, name="user_profile"),
    path('subscriptions', profile_views.premium_feed_list, name="subscriptions"),
    path('subscriptions/unsubscribe/<uuid:pk_id>', profile_views.unsubscribe_from_premium_feed, name="unsubscribe"),
    path('show_detail/<uuid:pk_id>', show_views.show_detail, name="manage_show_detail"),
    path('edit_show/<uuid:pk>/website', show_domain_views.ShowDomainsUpdateView.as_view(), name="manage_website_edit"),
    path('edit_show/<uuid:pk>', show_views.ShowDBUpdateView.as_view(), name="manage_show_edit"),
    path('create_show/', show_views.create_show, name="manage_show_create"),
    path('create_episode/<uuid:pk_id>', episode_views.create_episode, name="manage_episode_create"),
    path('episode_detail/<uuid:pk_id>', episode_views.episode_detail, name="manage_episode_detail"),
    path('episode_edit/<uuid:pk>', episode_views.EpisodeUpdateView.as_view(), name="manage_episode_edit"),
    path('edit_profile/', profile_views.user_profile, name="update_profile"),
    path('delete/<uuid:pk_id>', show_views.delete_show_view, name="manage_show_delete"),
    path('delete_episode/<uuid:pk_id>', episode_views.delete_episode_view, name="manage_episode_delete"),
   
]

