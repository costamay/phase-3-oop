class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def course_average(self):
        count = 0
        for student in self.students:
            count += student.marks

        print(count / len(self.students))


# creating student instances
s1 =  Student("Tyra", 18, 100)
s2 =  Student("Lucky", 20, 50)
s3 = Student("Alice", 23, 50)


# creating course instance
c = Course("Python programming")

# adding students to a course

c.add_student(s1)
c.add_student(s2)
c.add_student(s3)

# for student in c.students:
#     print(student.name)

c.course_average()