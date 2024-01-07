from django.shortcuts import render
from django.http import HttpResponse
# from .models import Form, Servise, Body, Trainer, Result


def main(request):
    return render(request, 'index.html') 
