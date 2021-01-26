# student_management_system


Usage Instructions
------------------

    1. Admin access to view DB : shared in mail
    
    2. URL to get student details 
    
      http://3.16.129.118:8000/student-details-using-id/<student_id>
      
      eg : http://3.16.129.118:8000/student-details-using-id/5/
     
      Sample Result :
        {"full_name": "Alyss Harcombe", "email": "aharcombe4@toplist.cz", "gender": "Female", "school_name": "Amos Comenius Memorial School", "school_phone": "933-3815", "books_read": "Big Nothing", "book_pages": 2427}
        
      Note : If student details is not available for given student_id : Error message is given 
               eg : {"Error": "No data available"}
        
     3. URL to HTML Form :
          http://3.16.129.118:8000/form/ 
          
          Notes : If no data is available for given input proper Error message and navigation is implemented :
                  Input name can be a first name of the user or full name (first_name full_name )
                  
             
  
  





Running On Local Machine Instructions
------------------

On Unix, Linux :
    # install django 
    
    $ python -m pip install Django
    
    python manager.py runserver 
    
    
    
For Detailed Documentation Make Use Of Pydoc :

    pydoc is not maintained 
    

