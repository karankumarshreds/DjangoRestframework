from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer as SS

# handling single model object 
def student_detail(req, pk):
  stu = Student.objects.get(id = pk)
  # convert to dict 
  serializer = SS(stu)
  # convert to json
  jsonData = JSONRenderer().render(serializer.data)
  return HttpResponse(jsonData, content_type='application/json')

