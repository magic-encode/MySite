
from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('about/', views.aboutView, name='about'),
    path('about/<str:pk>/', views.commentRemove,
         name='about-my-self-comment-remove'),
    path('download-resume/', views.myResumeDownloadView, name='download-resume'),
    path('project/', views.projectView, name='project'),
    path('contact/', views.contactView, name='contact'),
]
