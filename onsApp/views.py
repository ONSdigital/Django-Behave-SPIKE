from django.shortcuts import render
from .models import HomePage

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {"page": HomePage.objects.get(id=1)}
    return render(request, "onsApp/index.html", context)

def accessibility_statement(request):
    return render(request, 'onsApp/accessibility_statement.html')

def cookies(request):
    return render(request, 'onsApp/cookies.html')

def page_1(request):
    return render(request, 'onsApp/page_1.html')

def page_2(request):
    return render(request, 'onsApp/page_2.html')

def page_3(request):
    return render(request, 'onsApp/page_3.html')

def privacy_data(request):
    return render(request, 'onsApp/privacy_data.html')