from django.shortcuts import render, redirect, get_object_or_404
from .models import Application



def home(request):
    applications = Application.objects.all()
    return render(request, 'home.html', {'applications': applications})

