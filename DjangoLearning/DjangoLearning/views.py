from django.http import HttpResponse
from django.shortcuts import render

def home(request) : 
    # return HttpResponse("Hello, world. You are at DjangoLearning Home page")
    return render(request, 'index.html')