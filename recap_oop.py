class Dog:
    number_of_dogs = 0
    dog_list = []

    def __init__(self, name, breed):
        self._name = name
        self._breed = breed
        Dog.count_num_dogs()
        Dog.add_dog(self)

    # getter
    @property
    def name(self):
        return self._name
    

    # setter
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        self._name = value


    @classmethod
    def count_num_dogs(cls):
        cls.number_of_dogs += 1


    @classmethod
    def add_dog(cls, dog):
        cls.dog_list.append(dog)



    
   


    def bark(self):
        print("Woof")


dog1 = Dog("Rex", "Bulldog")
dog2 = Dog("Rolex", "German")
print(Dog.number_of_dogs)
new_list = [dog.__dict__ for dog in Dog.dog_list]
print(new_list)

# print(dog1.bark())
# dog2 = Dog()