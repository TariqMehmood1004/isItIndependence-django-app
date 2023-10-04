from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def greet(request, name):
    return render(request, "greet.html", {'name': name})
    
    