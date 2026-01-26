from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the quiz index.")

def index_2(request):
    return HttpResponse("Hello, world. You're at the quiz index part 2.")

def index_3(request):
    return HttpResponse("Welcome to index part 3.")   
