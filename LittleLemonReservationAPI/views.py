from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def g(request):
    return HttpResponse("<h1> Hello Fucking World </h1>")