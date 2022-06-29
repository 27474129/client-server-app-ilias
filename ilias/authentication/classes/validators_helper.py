# this file needs to avoid a circular models import


from ..models import Student, Professor


def get_matches(value):
    student_model_response = Student.objects.filter(username=value)
    professor_model_response = Professor.objects.filter(username=value)

    return [student_model_response, professor_model_response]