"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import  url
from my_app.views import process_query_using_studentid,login , home_view
from django.views.generic import TemplateView
app_name = 'my_app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-details-using-id/<int:student_id>/', process_query_using_studentid),
    path('form/', home_view, name ='form'),
    url(r'^login/', login, name = 'login')
  
]
#include('blog.urls')
#path(r'^student-details-using-id/(?P<post_id>\d+)/$', process_query_using_studentid),
#path('login/',login,name="login"),