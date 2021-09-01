from django.urls import path, re_path
from django.conf.urls import url
from . import views
from .views import show_frontend_views, rss_feed_views, social_media_views
urlpatterns = [

    path('rss/<uuid:pk_id>', rss_feed_views.show_feed, name="feed"),
    path('premium/<uuid:pk_id>', rss_feed_views.show_feed, name="premium_feed"),

    path('subscribe/<uuid:pk_id>', show_frontend_views.subscribe_to_premium_feed_view, name="subscribe"),

    path('redirect/facebook/<str:pk_id>', social_media_views.facebook_link_view, name="fb_redirect"),
    path('redirect/twitter/<str:pk_id>', social_media_views.twitter_link_view, name="twitter_redirect"),
    path('redirect/insta/<str:pk_id>', social_media_views.instagram_link_view, name="insta_redirect"),
    path('redirect/tiktok/<str:pk_id>', social_media_views.tiktok_link_view, name="tiktok_redirect"),
    path('redirect/youtube/<str:pk_id>', social_media_views.youtube_link_view, name="youtube_redirect"),
    path('redirect/reddit/<str:pk_id>', social_media_views.reddit_link_view, name="reddit_redirect"),
    
    path('<str:pk_id>/<uuid:ep_id>', show_frontend_views.show_episode_frontend_view, name="show_episode_frontend"),
    path('<str:pk_id>', show_frontend_views.show_frontend, name="show_frontend"),
    #re_path(r'^(?P<username>.*)', views.index, name="redirect_frontend")
    ]