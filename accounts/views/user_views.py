from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def landing_view(request):

    return render(request, "manage/home_page.html")


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