import os

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


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
        if request.user.is_authenticated:
            redirecturl = request.GET.get('redirect')
            try:
                return HttpResponseRedirect(os.getenv("HOSTNAME") + "/" + redirecturl)
            except TypeError:
                return HttpResponseRedirect(os.getenv("HOSTNAME"))
        else:
            if request.method == "POST":
                form = AuthForm(request.POST)
                if form.is_valid:
                    user = authenticate(
                        request,
                        username=form.data["username"],
                        password=form.data["password"],
                    )
                    if user is not None:
                        print(request)
                        login(request, user)
                        redirecturl = request.GET.get('redirect')
                        try:
                            print("yes")
                            return HttpResponseRedirect(os.getenv("HOSTNAME") + "/" + redirecturl)
                        except TypeError:
                            print("no")
                            print(redirecturl)
                            return HttpResponseRedirect(os.getenv("HOSTNAME"))
                    else:
                        print("Go away")
            elif request.method == "GET":
                redirecturl = request.GET.get('redirect')
                form = AuthForm()
            return render(request, "auth.html", {"form": form, "hostname": os.getenv("HOSTNAME"), "request":request, 'redirecturl':redirecturl})
            
