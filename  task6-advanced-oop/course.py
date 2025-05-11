from typing import List
from student import Student

# ....Course Class

class Course:
    def __init__(self, course_code: str, course_name: str):
        self.course_code = course_code
        self.course_name = course_name
        self.enrolled_students: List[Student] = [] 

    def enroll_student(self, student: Student) :
        self.enrolled_students.append(student)

    def __str__(self):
        return f"Course {self.course_name} ({self.course_code})"
    