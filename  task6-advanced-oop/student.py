from person import Person

# .....Student class (inherits from Person)

class Student(Person):
    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id

    def get_role(self):
        return "student"

    def __str__(self):
        return f"Student {self.name}, ID: {self.student_id}, email: {self.email}"