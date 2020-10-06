from django.shortcuts import render
from django.http import HttpResponse
import Files.renderfile, Files.formuploadtext, Files.dashboard, Files.auth
# Create your views here.
def index(request):
    return Files.formuploadtext.main(request)
def File(request, filename):
    return(Files.renderfile.renderFile(request, filename))
def dashboard(request):
    return(Files.dashboard.main(request))
def auth(request):
    return(Files.auth.main(request))