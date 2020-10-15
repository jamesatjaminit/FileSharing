import os

from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Files.models import File


def main(request):
    if request.user.is_authenticated:
        result = File.objects.filter(belongsto=request.user.id)
        paginator = Paginator(result, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # result[0].description
        return render(request, "dashboard.html",
                      {"entries": result, 'page_obj': page_obj, "hostname": os.getenv("HOSTNAME"), "request": request})
    else:
        return HttpResponseRedirect(os.getenv("HOSTNAME") + "/files/login?redirect=files/dashboard&errorcode=0")
