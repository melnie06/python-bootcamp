class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def introduce(self):
        return f'Hello, I am {self.first_name} {self.last_name}'
    
person = Person("Juan", "Miguel")
person.introduce()

print(person.introduce())