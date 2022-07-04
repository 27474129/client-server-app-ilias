from django.shortcuts import render, redirect
from .functions import *
from django.core.files.storage import FileSystemStorage
from .models import *


def student(request):
    if (request.method == "POST" and "file" in request.FILES and "username" in request.session):
        fss = FileSystemStorage(base_url=f"documents/{request.session[ 'username' ]}/math/lab1", \
                                location=f"documents/{request.session[ 'username' ]}/math/lab1")

        file = request.FILES[ "file" ]

        file_name = fss.save(file.name, file)


        url = fss.url(file_name)
        upload_time = fss.get_created_time(file_name)

        StudentFile(file=url, who_uploaded=request.session[ "username" ], upload_time=upload_time).save()


    is_user_authenticated = check_if_the_user_is_authenticated(request)
    return render(request, "student/student.html") if is_user_authenticated == True else is_user_authenticated
