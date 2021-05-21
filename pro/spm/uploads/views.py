from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, request


def home_view(request,*args, **kwargs):
    return render(request, "index.html", {})