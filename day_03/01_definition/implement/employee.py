
'''
#
class Employee:
    def __init__(self, name, id): #"self" the object that can be call to the function
        print(f"Employee {name} created with id {id}")


employee1 = Employee("Richard", "1234")
employee1.name = "Richard"
employee1.id = "1234"


employee2 = Employee("Jelly", "9876")
employee2.name = "Jelly"
employee2.id = "9876"
'''


class Employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(f"Employee {name} created with id {id}")
    
    
employee1 = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")