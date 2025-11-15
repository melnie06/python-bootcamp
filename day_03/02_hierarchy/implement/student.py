class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def introduce(self):
        return f"I'm {self.first_name} {self.last_name}!"

class Student(Person):
    def introduce(self):
        # return f"Hello, I am student"
        # return (super().introduce())
        return super().introduce() + ' I am a student'
    
student = Student("Jack", "Chan")
print(student.introduce())