from django.shortcuts import render, redirect
from .models import Student, Professor



def authentication(request):
    context = {}
    if (request.path == "/student_auth"):
        context[ "role" ] = "student"
    else:
        context[ "role" ] = "professor"


    if ("username" in request.session):
        if (context[ "role" ] == "student"):
            return redirect("student_page")
        else:
            return redirect("professor_page")

    if (request.method == "POST" and "username" not in request.session):
        entered_username = request.POST[ "username" ]
        entered_password = request.POST[ "password" ]


        if (context[ "role" ] == "student"):
            model = Student
        else:
            model = Professor

        match = model.objects.filter(username=entered_username).filter(password=entered_password)

        if (len(match) != 0):
            user = match[ 0 ]
        else:
            context[ "is_correct_userdata" ] = False
            return render(request, "authentication/authentication.html", context)

        if (user.username == entered_username and user.password == entered_password):
            request.session.set_expiry(86400)
            request.session[ "username" ] = entered_username
            context["is_correct_userdata"] = True
            if (context[ "role" ] == "student"):
                return redirect("student_page")
            else:
                return redirect("professor_page")


    context["is_correct_userdata"] = True
    return render(request, "authentication/authentication.html", context)


def logout(request):
    if ("username" in request.session):
        del request.session[ "username" ]

        if (request.session[ "role" ] == "student"):
            return redirect("student_auth_page")
        return redirect("professor_auth_page")
    else:
        return redirect("student_auth_page")


def root(request):
    return redirect("student_auth_page")