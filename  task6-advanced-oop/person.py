from abc import ABC, abstractmethod
from typing import List

# ....Base Class
class Person(ABC):
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} ({self.email})"
    
    def __hash__(self):
        return hash(self.email)
    
    def __eq__(self, other):
        return isinstance(other, Person) and self.email == other.email

    @abstractmethod
    def get_role(self):
        pass

#.....Student class (inherits from Person)

# .....Instructor class (Inherits from Person)

#  .....Course Class

# ....Enrollment class (handles student-course relationships)

# .....TeachingAssistant class (inherits from both Student and Instructor)

# .....Main program
