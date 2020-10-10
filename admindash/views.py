from django.http import request
from django.shortcuts import render
import admindash.admindash
# Create your views here.
def index(request):
    return(admindash.admindash.main(request))
def text(request):
    return(admindash.admindash.text(request))
def deletetext(request):
    return(admindash.admindash.deletetext(request))