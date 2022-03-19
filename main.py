from mimetypes import init


class Student:
    def __init__(self, student_name, enrollment_year):
        self.student_name = student_name
        self.enrollment_year = enrollment_year

    def print_student_info(self):
        print(f"Student's name: {self.student_name}")
        print(f"Enrollment year: {self.enrollment_year}")
        print("******************")


def sum_numbers(num_a, num_b):
    return num_a + num_b

input_a = int(input("Number a?: "))
input_b = int(input("Number b?: "))

print(sum_numbers(input_a, input_b))

new_student = Student("Abraham Ramos", 2021)

new_student.print_student_info()