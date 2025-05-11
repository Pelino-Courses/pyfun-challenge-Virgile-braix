from person import Person 
# .... TeachingAssistant class(inherits from both Student and Instructor)

class TeachingAssistant(Person):
    def __init__(self, name: str, email: str, student_id: str, employee_id: str):
        super().__init__(name, email)
        self.student_id = student_id
        self.employee_id = employee_id

    def get_role(self):
        return "Teaching Assistant"

    def __str__(self):
        return f"TA {self.name}, Student ID: {self.student_id}, Employee ID:{self.employee_id}, Email: {self.email}"
