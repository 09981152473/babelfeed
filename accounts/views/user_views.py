from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from shows_frontend.views import show_frontend_views
from manage.models.shows_domain import ShowDomains
import re
from django.core.exceptions import ObjectDoesNotExist

def landing_view(request):
    domain = request.META['HTTP_HOST']
    if "www." in domain:
        # live deployment
        #httpys://wwww.  subdomain. babelfeed. com/adsfasdf
        splitDomainArr = domain.split(".")
        if len(splitDomainArr) == 4:
            try:
                subdomain = splitDomainArr[1]
                qs = ShowDomains.objects.get_with_subdomain_name(subdomain)
                return show_frontend_views.show_frontend(request, subdomain)
            except:
                return render(request, "access_denied.html") # should redirect to an access denied or show not found page
        else:
            # No subdomain has been entered, so we go to the landing page
            return render(request, "manage/home_page.html")  # should redirect
    else:
        # local enviroment
        splitDomainArr = domain.split(".")
        if len(splitDomainArr) == 2:
            try:
                subdomain = splitDomainArr[0]
                qs = ShowDomains.objects.get_with_subdomain_name(subdomain)
                return show_frontend_views.show_frontend(request, subdomain)
            except:
                return render(request,
                              "access_denied.html")  # should redirect to an access denied or show not found page
        else:
            # No subdomain has been entered, so we go to the landing page
            return render(request, "manage/home_page.html")  # should redirect



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_profile")
        else:
            return redirect("landing_view")
    else:
        form = AuthenticationForm()
        return render(request,'accounts/login.html', {'form': form})


def access_denied(request):
    return render(request, "access_denied.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        # is_superuser

        if form.is_valid():
            superuse = form.save(commit=False)
            superuse.is_staff = True
            superuse.is_superuser = True
            print(superuse.is_staff)
            superuse.save()
            return redirect("login")
        else:
            print("shit fucked up")

    else:
        form = UserCreationForm()
    return render(request,'accounts/register.html', {'form': form})