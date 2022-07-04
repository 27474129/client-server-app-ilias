from django.db import models


class StudentFile(models.Model):
    file = models.FileField()
    who_uploaded = models.CharField(max_length=50)
    upload_time = models.DateTimeField()