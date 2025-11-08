class Person:
    """This class represents a person with a name"""

    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hi " + self.name


class ConsoleGreeter:
    """This wrapper class can print greetings in a terminal"""

    def __init__(self, person):
        self.person = person

    def show_greeting(self):
        print(self.person.greet())
