from django.contrib import admin
from django.urls import path, include
# views 
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:pk>', views.student_detail),
    path('student/', views.student_list)
]
