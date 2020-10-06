import django.http
from django import forms
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from Files.models import File
import random
import os.path
from os import path
def randomstring():
    random_string = ''
    for _ in range(30):
        # Considering only upper and lowercase letters
        random_integer = random.randint(97, 97 + 26 - 1)
        flip_bit = random.randint(0, 1)
        # Convert to lowercase if the flip bit is on
        random_integer = random_integer - 32 if flip_bit == 1 else random_integer
        # Keep appending random characters using chr(x)
        random_string += (chr(random_integer))
    return(random_string)
class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '100'}), label='Text', required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Description', required=True)
def main(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid:
            filename = randomstring()
            BaseName = "Files/Uploads/"
            while path.exists(BaseName + filename):
                filename = randomstring()
            tempfile = open(BaseName + filename, "w")
            tempfile.write(form.data['text'])
            tempfile.close()
            fileDB = File(name=filename, location=BaseName + filename, description=form.data['description'])
            fileDB.save()
            return HttpResponseRedirect("/files/f/" + filename)
        else:
            print(form._errors)
    elif request.method == 'GET':
        form = TextForm()
    return(render(request, "text.html", {'form': form}))