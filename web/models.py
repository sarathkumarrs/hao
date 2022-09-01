from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.
class Category(models.Model):
    image = models.ImageField(upload_to="categories")
    title = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('web:jobs_list_by_category', args=[self.slug])

class Job(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE,related_name = 'jobs')
    title = models.CharField(max_length=128)
    description = models.TextField()
    vacancies = models.CharField(max_length=4)
    experience = HTMLField()
    documents =  HTMLField()
    skill =  HTMLField()
    language =  HTMLField()
    sallery =  models.TextField()
    age = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('web:jobsingledy',args=[self.id])

class Social(models.Model):
    facebook = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    twitter = models.URLField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.phone

class Company(models.Model):
    about = HTMLField()
    home_image = models.ImageField(upload_to="homeimage")
    about_image = models.ImageField(upload_to='aboutimage')
    employee_cout = models.CharField(max_length=6)
    location = models.CharField(max_length=20)
    area = models.CharField(max_length=20)
    no_of_buildings = models.CharField(max_length=5)

    def __str__(self):
        return self.about