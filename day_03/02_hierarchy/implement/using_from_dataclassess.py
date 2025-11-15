from dataclasses import dataclass

@dataclass #decorator
class Person:
    first_name: str
    last_name: str
    
    def introduce(self):
        return f"hello {self.first_name} {self.last_name}"
    

@dataclass
class Student(Person):
    student_id: int
    
    def introduce(self):
        return super().introduce() + " I am a student"
    
student = Student("First", "Last", 1234)
print(student)