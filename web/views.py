from django.shortcuts import render
from .models import Category, Job, Social , Company
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse
import os
from django.http import HttpResponse
# Create your views here.

def index(request):
    categories = Category.objects.all()
    social = Social.objects.last()
    about = Company.objects.last()

    context = {
        'categories' : categories,
        'social':social,
        'about':about
    }
    return render(request,'index.html', context)

def about(request):
    about = Company.objects.last()
    social = Social.objects.last()
    context = {
        'about' : about,
        'social':social
    }
    return render(request,'about.html',context)

def jobs(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    jobs = Job.objects.all()
    social = Social.objects.last()

    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        jobs = Job.objects.filter(category=category)

    context = {
        "category": category,
        "categories": categories,
        "jobs": jobs,
        "social":social
    }
    return render(request,'jobs.html',context)

def jobsingle(request,id):
    job = get_object_or_404(Job,id=id)
    social = Social.objects.last()

    context = {
        'job':job,
        'social':social
    }
    return render(request,'jobsingle.html',context)

def pdfview(request):
    filepath = os.path.join('static', 'Hoatai secure.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def aboutpdf(request):
    filepath = os.path.join('static', 'haotai.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')

def hiring(request):
    filepath = os.path.join('static', 'hiring.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')