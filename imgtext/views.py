from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image
from .imageToText import text1
from .opencvtext import openCv
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
# direct to htmls

class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangeView
    success_url = reverse_lazy('home')


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
    global file

    return render(request,"download.html")

def contact(request):

    return render(request,"contact.html")

def about(request):

    return render(request,"about.html")

def text2(request):
    text1()
    global file

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



