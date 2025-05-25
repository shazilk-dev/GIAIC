class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")


if __name__ == "__main__":
    student1 = Student("John", 85)
    student1.display()
    
    student2 = Student("Emma", 92)
    student2.display()
