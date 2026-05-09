from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout

from .forms import RegisterForm


def signup(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Compte créé avec succès."
            )

            return redirect("profile")

    else:

        form = RegisterForm()

    return render(
        request,
        "registration/signup.html",
        {"form": form}
    )


@login_required
def profile(request):

    return render(
        request,
        "registration/profile.html"
    )

def custom_logout(request):

    logout(request)

    messages.success(
        request,
        "Vous êtes déconnecté."
    )

    return render(
        request,
        "registration/logout.html"
    )