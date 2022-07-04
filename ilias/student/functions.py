from django.shortcuts import render, redirect


def check_if_the_user_is_authenticated(request):
    if ("username" in request.session):
        return True if request.session["role"] == "student" else redirect("professor_page")
    else:
        return redirect("student_auth_page")