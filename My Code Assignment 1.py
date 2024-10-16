class ZulelaZoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def get_number_of_animals(self):
        return len(self.animals)

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def list_animals(self):
        print(f"Listing all animals in {self.name}:")
        for animal in self.animals:
            print(f"{animal.get_name()}")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Mammal(Animal):
    def make_sound(self):
        return f"{self.name} makes a mammal sound!"

class Bird(Animal):
    def make_sound(self):
        return f"{self.name} chirps!"

class Reptile(Animal):
    def make_sound(self):
        return f"{self.name} hisses!"

class Enclosure:
    def __init__(self, name, location, size):
        self.name = name
        self.location = location
        self.size = size
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def list_animals(self):
        print(f"Animals in {self.name} enclosure:")
        for animal in self.animals:
            print(f"{animal.get_name()}")

    def count_animals(self):
        return len(self.animals)

class Zookeeper:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.animals = []

    def feed_animals(self):
        print(f"{self.name} is feeding animals:")
        for animal in self.animals:
            animal.eat()

    def assign_animal(self, animal):
        self.animals.append(animal)
class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        try:
            if not isinstance(animal, Animal):
                raise TypeError("Only Animal instances can be added.")
            self.animals.append(animal)
        except TypeError as e:
            print(f"Error: {e}")

import json

def save_animals_to_file(enclosures, filename):
    data = {}
    for enclosure in enclosures:
        data[enclosure.name] = [animal.__dict__ for animal in enclosure.animals]
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_animals_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    enclosures = []
    for enclosure_name, animals in data.items():
        enclosure = Enclosure(enclosure_name)
        for animal_data in animals:
            animal = Animal(animal_data['name'], animal_data['species'])
            enclosure.add_animal(animal)
        enclosures.append(enclosure)
    return enclosures

def find_zookeepers_with_three_as(zookeepers):
    return [zk for zk in zookeepers if zk.last_name.lower().count('a') == 3]

def main()
    lion = Animal("Lion", "Mammal")
    eagle = Animal("Eagle", "Bird")
    snake = Animal("Snake", "Reptile")

    mammal_enclosure = Enclosure("Mammal Enclosure")
    bird_enclosure = Enclosure("Bird Enclosure")
    reptile_enclosure = Enclosure("Reptile Enclosure")

    mammal_enclosure.add_animal(lion)
    bird_enclosure.add_animal(eagle)
    reptile_enclosure.add_animal(snake)

    enclosures = [mammal_enclosure, bird_enclosure, reptile_enclosure]

    save_animals_to_file(enclosures, "zoo_data.json")

    loaded_enclosures = read_animals_from_file("zoo_data.json")

    zookeepers = [
        Zookeeper("John", "Anderson"),
        Zookeeper("Jane", "Maraaaa"),
        Zookeeper("Alice", "Smith")
    ]
    special_zookeepers = find_zookeepers_with_three_as(zookeepers)
    for zk in special_zookeepers:
        print(f"Zookeeper with three 'a's: {zk.first_name} {zk.last_name}")

if __name__ == "__main__":
    main()



