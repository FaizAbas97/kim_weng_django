from django.shortcuts import render
from quiz.models import Student
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the quiz index.")

def index_2(request):
    return HttpResponse("Hello, world. You're at the quiz index part 2.")

def index_3(request):
    students = Student.objects.all()
    response_message = "Hi"
    for student in students:
        response_message = response_message + f"{student.first_name} {student.last_name}"
    return HttpResponse(response_message)   


