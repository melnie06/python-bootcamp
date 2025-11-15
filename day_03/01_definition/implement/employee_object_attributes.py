class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(f"Employee {name} created with ID {id}")

employee1 = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")