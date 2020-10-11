import os

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render


def renderFile(request, filename):
    try:
        file = open(os.getenv("BASE_PATH") + r"Files\Uploads\\" + filename)
        return render(request, "rendertext.html", {"text": file.read(), "hostname": os.getenv("HOSTNAME"), "request":request})
    except FileNotFoundError:
        return HttpResponseNotFound("Whoops, we can't find that file")
