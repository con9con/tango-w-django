from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Rango says hey world!")

def about(request):
    return HttpResponse("Rango says here is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.\
    <br/><a href='../../'>Rango</a>")
