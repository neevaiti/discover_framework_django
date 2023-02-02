from django.shortcuts import render
from django.http import HttpResponse
from mentorat.models import User

def hello(request):
    users = User.objects.all()
    return render(request, "mentorat/hello.html",
                  {"utilisateurs": users})

def about(request):
    return HttpResponse("<h1>À propos, contactez nous.</h1>")
