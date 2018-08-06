from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Page that links to Funder and Contributor pages.")

def contributor(request):
    return HttpResponse("This is the Contributor Page")

def funder(request):
    return HttpResponse("This is the Funder Page")

# Create your views here.
