from django.shortcuts import render
import requests
from datetime import datetime
import requests, json

def index(request):
    return render(request,'index.html')


def about(request):
    if request.method=="POST":
        print(request)
    return render(request,'about.html')


def content(request):
    return render(request,'content.html',{"current_time":datetime.now()})



