from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Page that links to Funder and Contributor pages.")

# Create your views here.
