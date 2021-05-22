from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, request, HttpResponseRedirect
from .forms import *
from django.views.generic import ListView, CreateView
from .models import Upload
from django.urls import reverse_lazy

def home_view(request,*args, **kwargs):
    return render(request, "index.html", {})

# def editing_view(request,*args, **kwargs):
    
    
#     if request.method == 'POST':
#         form = Form(request.POST, request.FILES)
  
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('success')
#     else:
#         form = Form()
    
#     return render(request, "editing.html", {})
# def success(request):
#     return HttpResponse('successfully uploaded')

def editing_view(request):
     if request.method == 'POST':
        form = Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

     else:
        form = Form() # A empty, unbound form
     return render(request, "editing.html", {'form ': form })