class Pet:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Pet is speaking")


class Dog(Pet):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        super().speak()
        print("Dog is speaking")

class Cat(Pet):
    pass


dog1 = Dog("Rex", "White")
print(dog1.color)
# dog1.speak()