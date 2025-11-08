class Employee:
    """Class representation for employee data"""
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

employee1 = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")

print("Employee 1 Name:", employee1.name)
print("Employee 2 Name:", employee2.name)

employee1.add_work("Create Slides")
employee1.add_work("Present report")



