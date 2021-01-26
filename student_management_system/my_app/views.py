from django.shortcuts import render
from django.http import HttpResponse
from my_app.utils.model_utils import get_student_details_by_id, get_student_details_by_name, get_student_details_by_id_form
from my_app.forms import InputFormStudentName
from django.http import JsonResponse




def process_query_using_studentid(request, student_id):

    try:
      return HttpResponse(get_student_details_by_id(student_id))
    except:
      return HttpResponse(JsonResponse({"Error":"No data available"}))


  
# Create your views here. 
def home_view(request): 
    context ={} 
    context['form']= InputFormStudentName() 
    return render(request, "home.html", context) 

def login(request):
   
    if request.method == "POST":
      #Get the posted form
      MyLoginForm = InputFormStudentName(request.POST)
      
      if MyLoginForm.is_valid():
            
            try:
              if MyLoginForm.cleaned_data['student_id'] :
                  data =get_student_details_by_id_form(MyLoginForm.cleaned_data['student_id'])
                  return render(request, 'result.html', data)

            except:
              pass
            try:
              data =get_student_details_by_name(MyLoginForm.cleaned_data['name'])
            except:
              return render(request, 'not_found.html')
      else:
            return render(request, 'not_found.html')
    else:
      MyLoginForm = InputFormStudentName()
		
   #return render(request, 'result.html', {"username" : username})
    return render(request, 'result.html', data)