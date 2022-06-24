from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    group = models.CharField(max_length=30)
    subjects = models.TextField()

    def __str__(self):
        return self.username