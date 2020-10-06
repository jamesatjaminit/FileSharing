from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
def renderFile(request, filename):
    try:
        file = open(r"D:\Projects\Mine\FileSharing\Files\Uploads\\" + filename)
        return(render(request, "file.html", {'text': file.read()}))
    except FileNotFoundError:
        return(HttpResponseNotFound("Whoops, we can't find that file"))