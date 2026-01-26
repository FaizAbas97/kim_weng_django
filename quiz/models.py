from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Quiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Question(models.Model):
    date = models.CharField(max_length=50)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    is_true = models.BooleanField()
