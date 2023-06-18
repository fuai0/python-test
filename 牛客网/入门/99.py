class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        print(hasattr(self, "age"))

        setattr(Employee, "age", int(input()))
        print(f"{self.name}'salary is {self.salary}, and his age is {self.age}")


e = Employee(input(), int(input()))
e.printclass()