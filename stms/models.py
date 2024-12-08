from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="teacher_subjects")


class Class(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    

class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="student_classes")


class Schedule(models.Model):
    day = models.CharField(max_length=10)
    start_hour = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="shedule_subjects")
    clas = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="shedule_classes")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="shedule_teachers")


class Grade(models.Model):
    mark = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="grade_students")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="grade_subjects")
    date = models.DateField()
    
