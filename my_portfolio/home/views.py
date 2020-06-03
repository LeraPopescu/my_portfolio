from django.shortcuts import render
from .models import Job, Project, BlogPost
from django.shortcuts import render, get_object_or_404

# Create your views here.
def home_view(request):
    jobs = Job.objects
    projects = Project.objects
    blog_posts = BlogPost.objects
    return render(request, 'home/home_view.html', {'jobs': jobs, 'projects': projects, 'posts': blog_posts})

def detail(request, blog_name):
    print(blog_name)
    #blog_name = get_object_or_404(BlogPost, pk = blog_name)
    return render(request, 'home/' + blog_name + '.html', {'job': blog_name})