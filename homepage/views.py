from django.shortcuts import render
from .models import Tutors

def homepage(request):
    tutors = Tutors.objects.all()
    return render(request, 'index.html', {'tutors': tutors})
