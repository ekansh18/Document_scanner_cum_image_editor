from django.shortcuts import redirect, render

# Create your views here.
from django.http import HttpResponse, request, HttpResponseRedirect
from .forms import UpForm
from .models import Upload

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

# def editing_view(request):
     
#      if request.method == 'POST':
#         # form = Form(data=request.POST, files=request.FILES)
#         form = UpForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('success')
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})

#      else:
#         form = UpForm() # A empty, unbound form
        
#      return render(request, "f.html", {'form ': form})

def success(request):
     return HttpResponse('successfully uploaded')

def editing_view(request):
    form=UpForm()
    
    if request.method=='POST':
        form=UpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success')
    return render(request, 'editing.html', {'form':form})