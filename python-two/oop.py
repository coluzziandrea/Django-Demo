class Sample():

    species = "mammal"

    def __init__(self, breed, name, radius=1):
        self.breed = breed
        self.name = name
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


x = Sample(breed="Lab", name="Sammy", radius=2.3)
# print(type(x))
# print(x.breed)
# print(x.name)
# print(x.species)
# print(x.area())


class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("DOG created")

    def whoAmI(self):
        # Overriding parent's method
        print("WOOF")


# dog1 = Dog()
# dog1.whoAmI()
# dog1.eat()
