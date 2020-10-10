import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def renderFile(request, filename):
    try:
        file = open(r"D:\Projects\Mine\FileSharing\Files\Uploads\\" + filename)
        return render(request, "file.html", {"text": file.read(), "hostname": os.getenv("HOSTNAME")})
    except FileNotFoundError:
        return HttpResponseNotFound("Whoops, we can't find that file")
