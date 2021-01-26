from django import forms 
  
# creating a form  
class InputFormStudentName(forms.Form): 
  
    student_id = forms.CharField(required=False)
    name = forms.CharField(max_length = 200,required=False) 
    #last_name = forms.CharField(max_length = 200,required=False) 
