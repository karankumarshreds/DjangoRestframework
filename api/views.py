from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from models import Student
from serializers import StudentSerializer as SS

# single model object 
def student_detail(req):
  stu = Student.objects.get(id = 1)
  serializer = SS(stu)
  jsonData = JSONRenderer().render(serializer.data)
  return HttpResponse(jsonData, content_type='application/json')