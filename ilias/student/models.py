from django.db import models

class StudentFile(models.Model):
    file = models.FileField(upload_to="student_files")
