def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls


@add_greeting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


if __name__ == "__main__":
    # Create a Person instance (with the decorated class)
    person = Person("John", 30)
    print(person.display_info())
    print(f"Greeting: {person.greet()}")
    
    # Add the decorator to another class after its definition
    Student = add_greeting(Student)
    
    # Create a Student instance (with the decorated class)
    student = Student("Alice", "A")
    print(f"Student name: {student.name}, Grade: {student.grade}")
    print(f"Greeting: {student.greet()}")
    
    # Show that the decorator modified the actual class
    print(f"\nPerson class has greet method: {'greet' in dir(Person)}")
    print(f"Student class has greet method: {'greet' in dir(Student)}")
