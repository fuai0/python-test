class stu:
    def __init__(self,name,id,goal,grade):
        self.name = name
        self.id = id
        self.goal = goal
        self.grade = grade

    def dayin(self):
        print(f"{self.name}'s student number is {self.id}, and his grade is {self.goal}. He submitted {len(self.grade)//2+1} assignments, each with a grade of {self.grade}")

stu1 = stu(input(),input(),int(input()),input())
stu1.dayin()