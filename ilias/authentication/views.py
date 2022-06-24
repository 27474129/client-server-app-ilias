from django.shortcuts import render, redirect
from .models import Student


def authentication(request):
    context = {}
    if ("username" in request.session):
        return redirect("subjects_page")


    if (request.method == "POST" and "username" not in request.session):
        entered_username = request.POST[ "username" ]
        entered_password = request.POST[ "password" ]

        match = Student.objects.filter(username = entered_username).filter(password = entered_password)

        if (len(match) != 0):
            student = match[ 0 ]
        else:
            context[ "is_correct_userdata" ] = False
            return render(request, "authentication/authentication.html", context)

        if (student.username == entered_username and student.password == entered_password):
            request.session.set_expiry(86400)
            request.session[ "username" ] = entered_username
            return redirect("subjects_page")
    context["is_correct_userdata"] = True
    return render(request, "authentication/authentication.html", context)


def logout(request):
    del request.session[ "username" ]
    return redirect("auth_page")


def subjects(request):
    if ("username" in request.session):
        return render(request, "authentication/subjects.html")
    else:
        return redirect("auth_page")