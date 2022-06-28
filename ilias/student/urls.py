from django.urls import path, include
from .views import *

urlpatterns = [


    path("student", student, name="student_page"),
]
