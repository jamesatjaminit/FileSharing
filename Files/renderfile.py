from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
def renderFile(filename):
    try:
        file = open(r"D:\Projects\Mine\FileSharing\Files\Uploads\\" + filename)
        return(HttpResponse(file.read()))
    except:
        return(HttpResponseNotFound("Whoops, we can't find that file"))