from __future__ import unicode_literals

from django.db import models
# Create your models here.
# -*- coding: utf-8 -*-


from django.db import models



# Create your models here.


class Job(models.Model):
    #id
    id=models.IntegerField(primary_key=True, default="")
    #company name
    company_name = models.CharField(max_length=200)
    #job position
    position = models.CharField(max_length=200)
    #Images
    image = models.ImageField(upload_to='images/')
    #summary
    summary=models.TextField(max_length=5000)
    #date
    date = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.company_name


class Project(models.Model):
    #company name
    project_name = models.CharField(max_length=200)
    #job position
    project_type = models.CharField(max_length=200)
    #summary
    project_summary=models.TextField(max_length=5000)
    #Images
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.project_name


class BlogPost(models.Model):

    blog_post_name=models.CharField(max_length=200)
    blog_post_descr=models.CharField(max_length=200,default="")
    blog_text=models.TextField(blank=True)
    blog_image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.blog_post_name
