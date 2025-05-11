from student import Student
from course import Course

# ... Enrollment class (handles Student-course relationships)

class Enrollment:
    def __init__(self):
        self.enrollments = {}

    def enroll(self, student: Student, course: Course):
        if student not in self.enrollments:
            self.enrollments [student] = []
        if course not in self.enrollments[student]:    
            self.enrollments[student].append(course)
            course.enroll_student(student)
    
    def get_course_for_student(self, student: Student):
        return self.enrollments.get(student, [])

    def __str__(self):
        return "\n".join([
            f"{student.name} is enrolled in {[course.course_name for course in courses]}" 
            for student, courses in self.enrollments.items()])