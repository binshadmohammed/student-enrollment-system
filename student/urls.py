from django.urls import path,include
from . import views

urlpatterns =[
    path('studentsreg',views.studentsreg,name="studentsreg"),

]
