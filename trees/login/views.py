from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def mainmenu(request):
    return render(request, "login.html")

# Create your views here.
