from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

def index(request):
    return HttpResponse("Index Page that links to Funder and Contributor pages.")

def contributor(request):
    text = "This is the Contributor Page"
    template = loader.get_template('guides/index.html')
    context = {
        'text': text,
    }
    return HttpResponse(template.render(context, request))

def funder(request):
    template = loader.get_template('guides/index.html')
    return HttpResponse("This is the Funder Page")

def timer(request):
    template = loader.get_template('guides/index.html')
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    # context = {
    #     'html': html,
    # }
    # return HttpResponse(template.render(context, request))
    return HttpResponse(html)

# Create your views here.
