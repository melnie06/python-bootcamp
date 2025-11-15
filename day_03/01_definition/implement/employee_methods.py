class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        print(f"Employee {name} created with ID {id}")

    def work(self):
        print(f"Working {self.name}...")
        
        
employee1 = Employee("Richard", "1234")
employee2 = Employee("Jelly", "9876")

employee1.work()
employee2.work()
