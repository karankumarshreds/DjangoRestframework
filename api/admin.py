from django.contrib import admin
from .models import Student

admin.site.register(Student)


## OR to have list like view with specific columns 

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#   list_display = ['id', 'name', 'roll']


