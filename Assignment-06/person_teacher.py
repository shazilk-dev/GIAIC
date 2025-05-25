class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    
    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")


if __name__ == "__main__":
    person = Person("Ali", 30)
    print("Person Information:")
    person.display_info()
    
    print("\n" + "-" * 30 + "\n")
    
    teacher = Teacher("Sara", 35, "Computer Science")
    print("Teacher Information:")
    teacher.display_info()
