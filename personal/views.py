from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'personal/includes/main.html')

def about(request):
    return render(request, 'personal/includes/about.html')

def contact(request):
    return render(request, 'personal/includes/contact.html')

def skills(request):
    return render(request, 'personal/includes/skills.html')

def projects(request):
    return render(request, 'personal/includes/projects.html')