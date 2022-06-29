from django.db import models
from authentication.classes.Validators import Validators



class Student(models.Model):
    valids = Validators()

    username = models.CharField(max_length=50, verbose_name="Student name", validators=[valids.check_username_length, \
                                                                                        valids.check_for_uniqueness])
    password = models.CharField(max_length=50, validators=[valids.check_big_letters_count, valids.check_number_count, \
                                                           valids.check_password_length])

    group = models.CharField(max_length=30)
    subjects = models.TextField()
    role = models.CharField(max_length=30, default="student")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username", "group"]

class Professor(models.Model):
    username = models.CharField(max_length=50, verbose_name="Professor name")
    password = models.CharField(max_length=50)
    groups = models.TextField()
    subject = models.CharField(max_length=50, default="physics")
    role = models.CharField(max_length=10, default="professor")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username", "subject"]