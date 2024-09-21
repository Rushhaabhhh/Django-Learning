from django.shortcuts import render

def all(request) : 
    return render(request, 'AppIndex.html')