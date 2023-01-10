#singal inheritance
class Employee: 
    increament = 5000
    no_of_leaves = 30
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
        def printdetails(self):
            print(f"Name is{self.name},age is{self.age} and salary is{self.salary}.")
            
            class Developer(Employee):
                pass
            emp = Employee("ramesh", 34, 45000)
            dev = Developer("naveen", 32, 35000)
            print(emp.name)
            emp.printdetails()
            print(dev.name)
            dev.printdetails()
            print(dev.increament)
            