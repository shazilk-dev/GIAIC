class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable
        self._salary = salary     # Protected variable
        self.__ssn = ssn          # Private variable
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        print(f"SSN: {self.__ssn}")


if __name__ == "__main__":
    emp = Employee("John Doe", 50000, "123-45-6789")
    
    # Access public variable
    print("Accessing public variable:")
    print(f"Name: {emp.name}")
    
    # Access protected variable
    print("\nAccessing protected variable:")
    print(f"Salary: {emp._salary}")
    
    # Try to access private variable
    print("\nTrying to access private variable directly:")
    try:
        print(f"SSN: {emp.__ssn}")
    except AttributeError as e:
        print(f"Error: {e}")
    
    # Name mangling - how to access private variable
    print("\nAccessing private variable with name mangling:")
    print(f"SSN: {emp._Employee__ssn}")
    
    # Using the display method
    print("\nUsing display_info method:")
    emp.display_info()
