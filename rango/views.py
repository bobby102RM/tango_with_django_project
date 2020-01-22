from django.shortcuts import render
from django.http import HttpResponse

def index(request):
      return HttpResponse("Rango says howdy pardner!  <a href='/rango/about/'>About</a>")
	  
def about(request):
    return HttpResponse("Rango says this is the about page pardner!   <a href='/rango/index/'>Home</a> ")
	