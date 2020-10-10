from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
import os

class AuthForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}),
        label="Username",
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        label="Password",
        required=True,
    )


def main(request):
    if request.path == "/files/logout":
        logout(request)
        return HttpResponseRedirect(os.getenv("HOSTNAME") + "/files/dashboard")
    else:
        if not request.user.is_authenticated:
            if request.method == "POST":
                form = AuthForm(request.POST)
                if form.is_valid:
                    user = authenticate(
                        request,
                        username=form.data["username"],
                        password=form.data["password"],
                    )
                    if user is not None:
                        login(request, user)
                        return HttpResponseRedirect(os.getenv("HOSTNAME") + "/files/dashboard")
                    else:
                        print("Go away")
            elif request.method == "GET":
                form = AuthForm()
            return render(request, "auth.html", {"form": form, "hostname": os.getenv("HOSTNAME")})
        else:
            return HttpResponseRedirect(os.getenv("HOSTNAME") + "/files/dashboard")
