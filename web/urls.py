from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'web'

urlpatterns = [
    path("",views.index,name='home'),
    path('roadmap/',views.pdfview,name='pdfview'),
    path("about/",views.about,name='about'),
    path("jobs/",views.jobs,name='jobs'),
    path('jobsingle/',views.jobsingle, name='jobsingle'),
    path('<slug:category_slug>/',views.jobs,name='jobs_list_by_category'),
    path('<int:id>',views.jobsingle,name='jobsingledy'),
]