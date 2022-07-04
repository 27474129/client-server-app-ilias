from django.core.exceptions import ValidationError
import re
from .Request import Request


class Validators:


    def check_for_uniqueness(self, value):
        request = Request()
        student_matches = request.send_request(
            request = f"SELECT * FROM authentication_student WHERE username='{value}';",
            is_need_response=False
        )
        professor_matches = request.send_request(
            request = f"SELECT * FROM authentication_professor WHERE username='{value}';",
            is_need_response=False
        )


        if (student_matches or professor_matches):
            raise ValidationError(
                "This username already exists"
            )

    def check_big_letters_count(self, value):
        big_letters_count = re.findall(r"[A-Z]", value)
        if (len(big_letters_count) < 1):
            raise ValidationError(
                "Your password must contain at least one big letter"
            )

    def check_password_length(self, value):
        if (len(value) < 10):
            raise ValidationError(
                "Your password must be at least 10 characters long"
            )


    def check_number_count(self, value):
        match = re.findall(r"[0-9]", value)
        if (len(match) < 1):
            raise ValidationError(
                "Your password must contain at least one number"
            )


    def checking_for_numbers(self, value):
        match = re.findall(r"[0-9]", value)
        if (len(match) != 0):
            raise ValidationError(
                "Name, cant contain numbers"
            )


    def check_if_username_consists_only_of_digits(self, value):
        match1 = re.findall(r"[a-z]", value)
        match2 = re.findall(r"[A-Z]", value)

        if (len(match1) != 0 or len(match2) != 0):
            raise ValidationError(
                "Record book number must contain digits the only"
            )

