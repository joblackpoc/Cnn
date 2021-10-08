from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def Index(request):
    return render(request,'person/index.html')

def About(request):
    return render(request, 'person/about.html')

def multistepformexample(request):
    return render(request,"person/multistepformexample.html")

def multistepformexample_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("multistepformexample"))
    else:
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        twitter=request.POST.get("twitter")
        facebook=request.POST.get("facebook")
        gplus=request.POST.get("gplus")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        cpass=request.POST.get("cpass")
        if password!=cpass:
            messages.error(request,"Confirm Password Doesn't Match")
            return HttpResponseRedirect(reverse('multistepformexample'))

        try:
            multistepform=MultiStepFormModel(fname=fname,lname=lname,phone=phone,twitter=twitter,facebook=facebook,gplus=gplus,email=email,password=password)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepformexample'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepformexample'))