from django.shortcuts import render
from .models import Job
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_view(request):
    jobs = Job.objects
    return render(request, 'home/home_view.html', {'jobs': jobs, 'ga_label': 'in-left'})