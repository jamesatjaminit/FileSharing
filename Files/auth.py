import os

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render


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
            redirectUrl = request.GET.get('redirect')
            try:
                return HttpResponseRedirect(os.getenv("HOSTNAME") + "/" + redirectUrl)
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
                        login(request, user)
                        redirectUrl = request.GET.get('redirect')
                        try:
                            return HttpResponseRedirect(os.getenv("HOSTNAME") + "/" + redirectUrl)
                        except TypeError:
                            return HttpResponseRedirect(os.getenv("HOSTNAME"))
                    else:
                        redirectUrl = ''
                        errormessage = "The username or password you entered is incorrect."
            elif request.method == "GET":
                redirectUrl = request.GET.get('redirect')
                errorcode = request.GET.get('errorcode')
                if errorcode == "0":
                    errormessage = "You need to be authenticated to view that page, please login."
                elif errorcode == "1":
                    errormessage = "That is a private paste, if you have access, please login."
                else:
                    errormessage = ""

                form = AuthForm()
            return render(request, "login.html", {"form": form, "hostname": os.getenv("HOSTNAME"), "request": request,
                                                  'redirectUrl': redirectUrl, 'errormessage': errormessage})
