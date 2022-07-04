from django.db import models
from authentication.classes.Validators import Validators



class Student(models.Model):
    valids = Validators()

    username = models.CharField(max_length=50, verbose_name="Record book number", validators=[valids.check_for_uniqueness, \
                                                                                valids.check_if_username_consists_only_of_digits])

    password = models.CharField(max_length=50, validators=[valids.check_big_letters_count, valids.check_number_count, \
                                                           valids.check_password_length])

    firstname = models.CharField(max_length=50, validators=[valids.checking_for_numbers])
    secondname = models.CharField(max_length=50, validators=[valids.checking_for_numbers])


    group = models.CharField(max_length=30)
    subjects = models.TextField()
    role = models.CharField(max_length=30, default="student")

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username", "group", "firstname", "secondname"]

class Professor(models.Model):
    username = models.CharField(max_length=50, verbose_name="Professor name")
    password = models.CharField(max_length=50)
    groups = models.TextField()
    subject = models.CharField(max_length=50)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username", "subject"]