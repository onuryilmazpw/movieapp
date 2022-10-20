from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("index")

def movies(request):
    return HttpResponse("movies")

def movie_details(request, slug):
    return HttpResponse("movie_details: " + slug)