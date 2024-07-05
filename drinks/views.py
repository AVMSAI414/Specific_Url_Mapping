from django.shortcuts import render

# Create your views here.
def thumbsup(request):
    return render(request,"thumbsup.html")

def maaza(request):
    return render(request,"maaza.html")
