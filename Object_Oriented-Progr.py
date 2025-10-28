class person:
    def __init__(self, name, age):

        self.name = name
        self.age = age

    def introduce (self):
        print(f"My name is {self.name } and I am {self.age} years old.")


person_1 = person("Alice", 30)

person_1.introduce()

person_2 = person("Bob", 25)

person_2.introduce()