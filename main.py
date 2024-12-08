#https://docs.google.com/document/d/1zOiZ1RvdDTMeEh9VD2_0JUQH1UkAFNeo2zEO4IBXuQE/edit?tab=t.0
import django_startup
from stms.models import Subject, Teacher, Student, Class, Schedule, Grade

def create_subject(name, description):
    if Subject.objects.filter(name=name).exists():
        print("Цей предмет вже існує!")
    else:
        Subject.objects.create(name = name, description = description) 

def create_teacher(name, surname, subject):
    if Subject.objects.filter(name=subject).exists():
        Teacher.objects.create(name=name, surname=surname, subject=subject)
    else:
        print("Такого предмета не існує, створіть будь ласка предмет!")

def create_class(name, year):
    if Class.objects.filter(name=name).filter(year=year).exists():
        print(f"Такий клас з {year} роком навчання вже існує!")
    else:
        Class.objects.create(name=name, year=year)

def create_student(name, surname, clas):
    if Class.objects.filter(name=clas).exists():
        Student.objects.create(name=name, surname=surname, clas=clas)
    else:
        print("Вказаного класу не існує!")

def create_shedule(day, start_hour, subject, clas, teacher):
    if (
        Subject.objects.filter(name=subject).exists() and
        Class.objects.filter(name=clas).exists() and 
        Teacher.objects.filter(name=teacher).exists()
    ):
        Schedule.objects.create(day=day, start_hour=start_hour,subject=subject, clas=clas, teacher=teacher)
    else:
        print("Чогось не вистачає в базі....")
        print(f"{subject} - {Subject.objects.filter(name=subject).exists()}")
        print(f"{clas} - {Class.objects.filter(name=clas).exists()}")
        print(f"{teacher} - {Teacher.objects.filter(name=teacher).exists()}")
        
name = input("Enter subject name \n")
description = input("Enter subject description\n")
create_subject(name, description)


