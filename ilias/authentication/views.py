from django.shortcuts import render, redirect
from .models import Student, Professor
from authentication.classes.Authentication import Authentication


def authentication(request):
    auth = Authentication()

    context = auth.get_user_role(request)

    is_authenticated = auth.is_authenticated(request, context)

    if (not is_authenticated):
        response = auth.authenticate(request, context)

        if (not response):
            context[ "is_correct_userdata" ] = False
            return render(request, "authentication/authentication.html", context)

        if (response == "GET"):
            context[ "is_correct_userdata" ] = True
            return render(request, "authentication/authentication.html", context)

        return redirect(response)

    else:
        return redirect(is_authenticated)



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