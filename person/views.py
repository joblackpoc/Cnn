from django.shortcuts import render

# Create your views here.
def Index(request):
    return render(request,'person/index.html')

def About(request):
    return render(request, 'person/about.html')