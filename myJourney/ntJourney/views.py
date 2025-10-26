# Handles display of learning journey and about me pages.
from django.shortcuts import render
from .models import LearningStep, AboutMe

# Home page
def index(request):      
    steps = LearningStep.objects.all().order_by('-date')
    return render(request, 'index.html', {'steps': steps})

# About Me page
def aboutMe(request):      
    about = AboutMe.objects.first()
    return render(request, 'aboutMe.html', {'about': about})
