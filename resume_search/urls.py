from django.contrib import admin
from django.urls import path
from resume_search import views

urlpatterns = [
    path("",views.index, name='resume_search'),
    path("about",views.about, name='about'),
    path("services",views.services, name='about')
]