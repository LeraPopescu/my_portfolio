from django.shortcuts import render
from .models import Job, Project
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_view(request):
    jobs = Job.objects
    projects = Project.objects
    return render(request, 'home/home_view.html', {'jobs': jobs, 'projects': projects})