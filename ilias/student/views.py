from django.shortcuts import render, redirect


def student(request):
    if ("username" in request.session):
        if (request.session["role"] == "student"):
            return render(request, "student/student.html")
        else:
            return redirect("professor_page")
    else:
        if (request.session["role"] == "student"):
            return redirect("student_auth_page")
        else:
            return redirect("professor_auth_page")
