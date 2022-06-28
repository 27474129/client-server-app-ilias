from django.shortcuts import render, redirect

def professor(request):
    if ("username" in request.session):
        if (request.session[ "role" ] == "professor"):
            return render(request, "professor/professor.html")
        else:
            return redirect("student_page")
    else:
        return redirect("professor_auth_page")