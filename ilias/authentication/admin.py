from django.contrib import admin
from .models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "group")
    list_display_links = ("id", "username", "group")
    search_fields = ("id", "username", "group")

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "subject")
    list_display_links = ("id", "username", "subject")
    search_fields = ("id", "username", "subject")



admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)