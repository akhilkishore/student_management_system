
from my_app.models import Student
from my_app.models import School
from my_app.models import Book
from django.http import JsonResponse

def get_student_details_by_id(input):
    student_object = Student.objects.get(id = input)
    
    full_name = student_object.first_name +" "+student_object.last_name
    email = student_object.email
    gender = student_object.gender 
    school_name = student_object.school 
    books_read = student_object.books

    school_object = School.objects.get(school = student_object.school )
    school_phone = school_object.phone

    book_object = Book.objects.get(title = student_object.books)
    book_pages = book_object.nop

    return JsonResponse({"full_name":full_name,"email":email,"gender":gender, "school_name":school_name, "school_phone":school_phone, "books_read":books_read , "book_pages":book_pages }) 


def get_student_details_by_id_form(input):
    student_object = Student.objects.get(id = input)
    
    full_name = student_object.first_name +" "+student_object.last_name
    email = student_object.email
    gender = student_object.gender 
    school_name = student_object.school 
    books_read = student_object.books

    school_object = School.objects.get(school = student_object.school )
    school_phone = school_object.phone

    book_object = Book.objects.get(title = student_object.books)
    book_pages = book_object.nop

    return {"full_name":full_name,"email":email,"gender":gender, "school_name":school_name, "school_phone":school_phone, "books_read":books_read , "book_pages":book_pages }


def get_student_details_by_name(name):

    if ' ' in name:
        fname = name.split(' ')[0]
        lname = name.split(' ')[1]
        student_object = Student.objects.get(first_name = fname, last_name=lname)
    else:
        student_object = Student.objects.get(first_name = name)

    full_name = student_object.first_name +" "+student_object.last_name
    email = student_object.email
    gender = student_object.gender 
    school_name = student_object.school 
    books_read = student_object.books

    school_object = School.objects.get(school = student_object.school )
    school_phone = school_object.phone

    book_object = Book.objects.get(title = student_object.books)
    book_pages = book_object.nop

    return {"full_name":full_name,"email":email,"gender":gender, "school_name":school_name, "school_phone":school_phone, "books_read":books_read , "book_pages":book_pages }

