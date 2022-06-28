from django.urls import path, include
from .views import *


urlpatterns = [
    path("professor", professor, name="professor_page"),
]