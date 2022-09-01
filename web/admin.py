from django.contrib import admin
from .models import Category, Job, Social, Company

# Register your models here.
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Social)
admin.site.register(Company)
