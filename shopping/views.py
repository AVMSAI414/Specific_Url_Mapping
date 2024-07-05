from django.shortcuts import render

# Create your views here.

def shirts(request):
    return render(request,"shirts.html")

def jeans(request):
    return render(request,"jeans.html")