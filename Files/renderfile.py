import os

from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render

from Files.models import File


def renderFile(request, filename):
    file = File.objects.filter(name=filename)
    errorcode = request.GET.get('errorcode')
    if errorcode == "1":
        errormessage = "You asked us to make a private paste, but since you're not logged in, we had to make it unlisted"
    else:
        errormessage = ""
    if file[0].visibility == 'private':
        if request.user.is_authenticated: 
            if file[0].belongsto == request.user.id or request.user.is_staff: # User is the correct user, display the file
                if not file[0].belongsto == request.user.id and request.user.is_staff:
                    viewbecausestaff = True
                else:
                    viewbecausestaff = False
                text = open(os.getenv("BASE_PATH") + r"Files\Uploads\\" + filename)
                return render(request, "rendertext.html", {"text": text.read(), "hostname": os.getenv("HOSTNAME"), "request":request, 'viewbecausestaff':viewbecausestaff})
            else:
                return(HttpResponseRedirect(os.getenv("HOSTNAME") + "/files/forbidden?errorcode=1")) # User doesn't have access to paste
        else:
            return(HttpResponseRedirect(os.getenv("HOSTNAME") + "/files/login?redirect=files/f/" + filename + "&errorcode=1")) # User is logged in
    try:
        text = open(os.getenv("BASE_PATH") + r"Files\Uploads\\" + filename)
        return render(request, "rendertext.html", {"text": text.read(), "hostname": os.getenv("HOSTNAME"), "request":request, "errormessage":errormessage})
    except FileNotFoundError:
        return HttpResponseNotFound("Whoops, we can't find that file")
