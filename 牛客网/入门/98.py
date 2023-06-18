from os import name
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        try:
            print(f"{self.name}'salary is {self.salary}, and his age is {age}")
        except:
            print("Error! No age")
            age = int(input())
            print(f"{self.name}'salary is {self.salary}, and his age is {age}")

e = Employee(input(),int(input()))
e.printclass()

