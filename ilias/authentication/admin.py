from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ("firstname", "secondname", "username", "group")
    list_display_links = ("firstname", "secondname", "username", "group")
    search_fields = ("firstname", "secondname", "username", "group")

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "subject")
    list_display_links = ("id", "username", "subject")
    search_fields = ("id", "username", "subject")



admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)