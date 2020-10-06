from django.contrib.auth import authenticate, login, logout
from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect

class AuthForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password', required=True)
def main(request):
    if request.path == '/files/logout':
        logout(request)
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthForm(request.POST)
            if form.is_valid:
                user = authenticate(request, username=form.data['username'], password=form.data['password'])
                if user is not None:
                    login(request, user)
                    return(HttpResponseRedirect("http://127.0.0.1:8000/files/dashboard"))
                else:
                    print("Go away")
        elif request.method == 'GET':
            form = AuthForm()
        return(render(request, "auth.html", {'form': form}))
    else:
        return(HttpResponseRedirect("http://127.0.0.1:8000/files/dashboard"))