from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello this is view insid my_app")

def simple_view(request):
    return HttpResponse("Simple View")