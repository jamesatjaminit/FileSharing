import django.http
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from Files.models import File


def main(request):
    if request.user.is_authenticated:
        result = File.objects.filter(belongsto=request.user.id)
        paginator = Paginator(result, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # result[0].description
        return render(request, "dashboard.html", {"entries": result, 'page_obj': page_obj})
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/files/login")
