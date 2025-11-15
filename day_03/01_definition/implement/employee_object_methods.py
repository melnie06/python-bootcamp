class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")


    def work(self, task):
        print(f"Working {task}...")
        self.tasks.append(task)

employee1 = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")

employee1.work("Create Slides")
employee2.work("Present Slides")    