from django.urls import path
from .views.user_views import landing_view, register, login_view, logout_view, access_denied

urlpatterns = [
    path('', landing_view, name="landing_view"),
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('access_denied/', access_denied, name="access_denied"),
]