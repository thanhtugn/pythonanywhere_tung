from django.shortcuts import render
from django.db import models

# Create your views here.
from django.http import HttpResponse
from .forms import UploadFileForm

def fileUploaderView(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2>Uploaded file successfully</h2>")
        else:
            return HttpResponse("<h2>Uploaded file not successfully</h2>")
        
    form = UploadFileForm()
    return render(request, 'fileUploaderTemplate.html', {'form' : form})



def upload(f):
    file = open(f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)
