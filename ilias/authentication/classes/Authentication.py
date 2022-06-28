from ..models import Professor, Student
from django.shortcuts import render, redirect


class Authentication:

    def get_user_role(self, request):
        context = {}

        if (request.path == "/student_auth"):
            context["role"] = "student"
        else:
            context["role"] = "professor"

        return context

    def is_authenticated(self, request, context):
        if ("username" in request.session):
            if (context["role"] == "student"):
                return "student_page"
            else:
                return "professor_page"
        else:
            return False

    def authenticate(self, request, context):
        if (request.method == "POST" and "username" not in request.session):
            entered_username = request.POST["username"]
            entered_password = request.POST["password"]

            if (context["role"] == "student"):
                model = Student
            else:
                model = Professor

            match = model.objects.filter(username=entered_username).filter(password=entered_password)

            if (len(match) != 0):
                user = match[0]
            else:
                return False

            if (user.username == entered_username and user.password == entered_password):
                request.session.set_expiry(86400)
                request.session["username"] = entered_username

                if (context["role"] == "student"):
                    return "student_page"
                else:
                    return "professor_page"

        return "GET"