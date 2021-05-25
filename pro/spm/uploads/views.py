from django.http.response import StreamingHttpResponse
from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, request, HttpResponseRedirect
from .forms import UpForm, UpImage, Scup
from .models import Upload

def home_view(request,*args, **kwargs):
    return render(request, "index.html", {})


def success(request):
     return render(request, 'imgshow.html', {'img_obj':img_obj})
    # return HttpResponse("success")

def editing_view(request):
    form=UpForm()
    
    if request.method=='POST':
        form=UpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_obj=form.instance
            # return HttpResponseRedirect('success')
            return render(request, 'imgshow.html', {'img_obj':img_obj})
    return render(request, 'editing.html', {'form':form})

def came(request):
       form=UpImage()
    
       if request.method=='POST':
         form=UpImage(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            img_obj=form.instance
            # return HttpResponse('success')
            return render(request, 'imgshow.html', {'img_obj':img_obj})
       return render(request, "cam.html",{'form':form})
   
def scan(request):
       form=Scup()
    
       if request.method=='POST':
         form=Scup(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            img_obj=form.instance
            # return HttpResponse('success')
            return render(request, 'docshow.html', {'img_obj':img_obj})
       return render(request, 'scann.html',{'form':form})  

def camsc(request):
       form=Scup()
    
       if request.method=='POST':
         form=Scup(request.POST,request.FILES)
         if form.is_valid():
            form.save()
            img_obj=form.instance
            # return HttpResponse('success')
            return render(request, 'docshow.html', {'img_obj':img_obj})
       return render(request, "cam.html",{'form':form})