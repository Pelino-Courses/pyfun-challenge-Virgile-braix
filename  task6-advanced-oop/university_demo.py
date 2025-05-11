from student import Student
from instructor import Instructor
from teaching_assistant import TeachingAssistant
from course import Course
from enrollment import Enrollment

if __name__ == "__main__":
    print("=== University Enrollment System ===")
    # User login
    name = input("Enter your name: ")
    email = input("Enter your university email: ")
    role = input("Enter your role (student/instructor/ta):").strip().lower()
    user = None

    if role == "student":
        student_id = input("Enter your student ID: ")
        user = Student(name, email, student_id)
    elif role == "instructor":
        employee_id = input("Enter your employee ID: ")
        user = Instructor(name, email, employee_id)
    elif role == "ta":
        student_id = input("Enter your student ID: ")
        employee_id = input("Enter your employee ID: ")
        user = TeachingAssistant(name, email, student_id, employee_id)
    else:
        print("Invalid role. Exiting.") 
        exit()

    print(f"\n Welcome, {user.get_role()} {user.name}! ")

    # Create demo courses
    course1 =  Course("IT101", "Introduction to Python")
    course2 = Course("MATH201", "Laplace Transform")

    # Enrollments
    enrollment = Enrollment()

    # Only Students and TAs can enroll

    if isinstance(user, Student):
        print("\n Available Courses: ")
        print(f"1. {course1}")
        print(f"2. {course2}")
        selected_courses = input("Enter course numbers to enroll...(example: 1, 2): ")
        for choice in selected_courses.split(","):
            choice = choice.strip()
            if choice == "1":
                enrollment.enroll(user, course1)
            elif choice == "2":
                enrollment.enroll(user, course2)


    print("\n --- Enrollment Status ---")
    print(enrollment)

    print("\n --- Role info ---")
    print(user)
