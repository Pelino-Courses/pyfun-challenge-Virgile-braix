from person import Person

# ..... Instructor class (Inherits from person)

class Instructor (Person):
    def __init__(self, name: str, email: str, employee_id: str):
        super().__init__(name, email)
        self.employee_id = employee_id

    def get_role(self):
        return "Instructor"

    def __str__(self):
        return f"Instructor {self.name}, ID: {self.employee_id}, Email: {self.email}"