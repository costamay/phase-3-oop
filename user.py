class User:
    def __init__(self, name):
        self.name = name


    def status(self):
        print("User is active")


class Student(User):

    def __init__(self, name, gender):
        # self.name = name
        super().__init__(name)
        self.gender = gender

    def status(self):
        # super method
        
        print("Student is active")
        super().status()



class Teacher(User):
    pass


s1 = Student("Titus", "Male")
print(s1.status())