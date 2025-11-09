class Cat:
    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight

    def grow(self):
        self.age += 1
        if self.age >= 2:
            self.weight += 0.2
        else:
            self.weight += 1


    def print_info(self):
        print("Cat Info:")
        print(f'Name: {self.name}')
        print(f'Breed: {self.breed}')
        print(f'Age: {self.age}')
        print(f'Weight: {self.weight:.2f}\n')

Cat = Cat(name='Romi', breed='Siamese_cat', age=1, weight= 4.6)
for i in(range(5)):
    Cat.print_info()
    Cat.grow()
