import django.http
from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from Files.models import File
import Files
import os

def text(request):
    if request.user.is_staff:
        result = File.objects.all()
        paginator = Paginator(result, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # result[0].description
        return render(request, "textadmin.html", {"entries": result, 'page_obj': page_obj})
    elif not request.user.is_authenticated:
        return HttpResponseRedirect("http://127.0.0.1:8000/files/login")
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/files/")
def deletetext(request):
    if request.user.is_staff:
        fieldid = request.GET.get('id')
        if fieldid == '':
            return(HttpResponse("ID field in URL was blank"))
        try:
            object = File.objects.get(id=fieldid)
        except Files.models.File.DoesNotExist:
            return(HttpResponse("Could not find item matching id in database"))
        try:
            os.remove(r'D:\Projects\Mine\FileSharing\Files\Uploads\\' + object.name)
        except FileNotFoundError:
            object.delete()
            return(HttpResponse("Couldn't delete file on disk, deleted database entry"))
        object.delete()
        return(HttpResponse("Successfully deleted file!"))