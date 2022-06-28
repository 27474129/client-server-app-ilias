from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    group = models.CharField(max_length=30)
    subjects = models.TextField()
    role = models.CharField(max_length=30, default="student")

    def __str__(self):
        return self.username


class Professor(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    groups = models.TextField()
    subject = models.CharField(max_length=50, default="physics")
    role = models.CharField(max_length=10, default="professor")

    def __str__(self):
        return self.username