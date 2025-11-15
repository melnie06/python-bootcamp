class Parent:   
    def parent_method(self):
        print("Parent method")
        
    def parent_method2(self):
        print("Parent method")
        
    

class Child(Parent):   
    def child_method(self):
        print("Child method")
        
child = Child()
child = Parent.method2()