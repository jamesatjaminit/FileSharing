import django.http
from django import forms
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from Files.models import File
def main(request):
    if request.user.is_authenticated:
        result = File.objects.filter(belongsto=request.user.id)
        # result[0].description
        return(render(request, "dashboard.html", {'entries': result}))
    else:
        return(HttpResponseRedirect('http://127.0.0.1:8000/files/login'))