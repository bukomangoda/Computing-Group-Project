from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image
from .imageToText import text1
from .opencvtext import openCv
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# direct to htmls



def home(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            
            text1()
            return render(request,"download.html",{"obj":obj})
    else:
        form=ImageForm()
    img=Image.objects.all()
    

    return render(request,"index.html",{"img":img,"form":form})

def openC(request):
    openCv()

    return render(request,"download.html")

def text2(request):
    text1()

    return render(request,"download.html")

def register(request):
    form = UserCreationForm
    if request.method == "POST":
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            
            messages.success(request, "User has been Registered")
            return redirect('home')
    return render(request, 'registration/register.html', {'form': form})






