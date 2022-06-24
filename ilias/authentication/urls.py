from django.urls import path
from .views import *

urlpatterns = [
    path("auth", authentication, name="auth_page"),
    path("subjects", subjects, name="subjects_page"),
    path("logout", logout, name="logout_func")
]