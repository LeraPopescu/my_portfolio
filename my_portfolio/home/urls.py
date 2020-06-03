from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('<str:blog_name>/', views.detail, name='blog'),
    path('<str:project_name>/', views.detail, name='project'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.SASS_PROCESSOR_ROOT, document_root=settings.SASS_PROCESSOR_ROOT)