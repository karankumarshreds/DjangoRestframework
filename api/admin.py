from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'roll']

## OR simply 

# admin.site.register(Search)
# admin.site.register(Profile)
# admin.site.register(Post)
# admin.site.register(Likes)

