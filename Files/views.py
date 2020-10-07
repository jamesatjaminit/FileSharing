from django.http import HttpResponse
from django.shortcuts import render

import Files.auth
import Files.dashboard
import Files.formuploadtext
import Files.renderfile


# Create your views here.
def index(request):
    return Files.formuploadtext.main(request)
def File(request, filename):
    return(Files.renderfile.renderFile(request, filename))
def dashboard(request):
    return(Files.dashboard.main(request))
def auth(request):
    return(Files.auth.main(request))