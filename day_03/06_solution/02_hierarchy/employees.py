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
    """Class representation for recruiter data"""

    def recruit(self):
        self.add_work("recruit")


class Developer(Employee):
    """Class representation for developer data"""

    def code(self):
        self.add_work("code")


class Manager(Employee):
    """Class representation for manager data"""

    def manage(self):
        self.add_work("manage")
