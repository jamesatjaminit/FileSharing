import os

from django.http import (HttpResponseNotFound,
                         HttpResponseRedirect)
from django.shortcuts import render

from Files.models import File


def renderFile(request, filename):
    file = File.objects.filter(name=filename) # Gets the file from the db
    errorCode = request.GET.get('errorCode') # Gets the error code if any
    if errorCode == "1": # Happens when user is authenticated but wants a private paste
        errormessage = "You asked us to make a private paste, but since you're not logged in, we had to make it " \
                       "unlisted "
    else:
        errormessage = ""
    if file[0].visibility == 'private': # If the paste is private we need to make some more checks
        if not file[0].belongsto == 0: # Checks if the file belongs to user id 0 which is an unauthed user
            if request.user.is_authenticated: # Check if they are logged into and account
                if file[0].belongsto == request.user.id or request.user.is_staff: # Checks if the user is the owner of the file OR staff
                    if not file[0].belongsto == request.user.id and request.user.is_staff: # If the it doesn't belong to the user but they are staff
                        viewBecauseStaff = True # Set to true
                    else:
                        viewBecauseStaff = False
                    text = open(os.getenv("BASE_PATH") + r"Files\Uploads\\" + filename) # Opens the file
                    try:
                        text = open(os.getenv("BASE_PATH") + r"Files\Uploads\\" + filename)
                        return render(request, "rendertext.html",
                                      {"text": text.read(), "hostname": os.getenv("HOSTNAME"), "request": request,
                                       "errormessage": errormessage})
                    except FileNotFoundError:
                        return HttpResponseNotFound("Whoops, we can't find that file")
                else:
                    return (HttpResponseRedirect(
                        os.getenv("HOSTNAME") + "/files/forbidden?errorCode=1"))  # Redirect user as they don't have access
            else:
                return (HttpResponseRedirect(os.getenv(
                    "HOSTNAME") + "/files/login?redirect=files/f/" + filename + "&errorCode=1"))  # User isn't logged in, redirect them to the login page
    try:
        text = open(os.getenv("BASE_PATH") + r"Files\Uploads\\" + filename)
        return render(request, "rendertext.html",
                      {"text": text.read(), "hostname": os.getenv("HOSTNAME"), "request": request,
                       "errormessage": errormessage})
    except FileNotFoundError:
        return HttpResponseNotFound("Whoops, we can't find that file")
