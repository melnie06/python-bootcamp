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
    
class Recruiter(Employee):
    def recruit(self):
        self.add_work("recruit")
    
    
class Developer(Employee):
    def code(self):
        self.add_work("developer")
        
        #current = calls the "self define"
        #super = calls the "Parent"
    
class Manager(Employee):
    def manage(self):
        self.add_work("manager")
        

employee = Recruiter("Jackie", "12345")
employee.recruit()

employee = Developer("Chan", "758910")
employee.code()

employee = Manager("Peter", "9876541")
employee.manage()
