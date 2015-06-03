from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("This is the homepage.\
    <br/><a href='/rango/'>Rango</a>\
    <br/><a href='/rango/about'>About</a>"

    )
