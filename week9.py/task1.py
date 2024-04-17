class students:
    def __init__(self):
        self.name = "Noor"
        self.age = "20"
        self.grade = "A+"

    def welcome(self):
        print(f"I am {self.name}. My age is {self.age}. My grade is {self.grade}")

student1=students()
student1.welcome()