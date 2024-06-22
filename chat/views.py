from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('<h1>Django and Python Chat App</h1> <iframe src="https://deadsimplechat.com/VgF7WaZpF" width="100%" height="600px"></iframe>')