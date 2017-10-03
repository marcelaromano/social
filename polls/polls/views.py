from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls home page.")


def contact(request):
    return HttpResponse("<h1>Contactanos.</h1><p>Ahora.</p>")


def about(request):
    return render(request, 'about.html')
