from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# reurns a http response says hello world when calling january
def january(request):
    return HttpResponse("eat no meat for the entire month of january")

def february(request):
    return HttpResponse("walk for at least 20 minutes every day")

def march(request):
    return HttpResponse("learn django for at least 20 minutes every day")