class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof woof!")
    
    def display_info(self):
        print(f"Dog: {self.name}, Breed: {self.breed}")
    
    def fetch(self, item):
        print(f"{self.name} is fetching the {item}!")


if __name__ == "__main__":
    dog1 = Dog("Max", "Golden Retriever")
    dog2 = Dog("Bella", "German Shepherd")
    
    dog1.display_info()
    dog1.bark()
    dog1.fetch("ball")
    
    print()
    
    dog2.display_info()
    dog2.bark()
    dog2.fetch("stick")
