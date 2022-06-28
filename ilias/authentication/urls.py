from django.urls import path, include
from .views import *


urlpatterns = [
    path("student_auth", authentication, name="student_auth_page"),
    path("professor_auth", authentication, name="professor_auth_page"),
    path("logout", logout, name="logout_func"),
    path("", root, name="root_page"),
]