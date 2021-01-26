from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    school = models.CharField(max_length=300)
    books = models.CharField(max_length=300)
    class Meta:
            db_table = 'student_details'

class School(models.Model):
    REGIONID = models.IntegerField()
    school = models.CharField(max_length=300, primary_key=True)
    email = models.CharField(max_length=300)
    principal = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address2 = models.CharField(max_length=300)
    class Meta:
            db_table = 'school_details'

class Book(models.Model):
    title = models.CharField(max_length=300, primary_key=True)
    author_name = models.CharField(max_length=300)
    dop = models.CharField(max_length=100)
    nop = models.CharField(max_length=50)
    class Meta:
            db_table = 'book_details'






