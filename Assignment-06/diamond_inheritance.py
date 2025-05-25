class A:
    def show(self):
        print("This is class A show method")


class B(A):
    def show(self):
        print("This is class B show method")


class C(A):
    def show(self):
        print("This is class C show method")


class D(B, C):
    pass


if __name__ == "__main__":
    # Create instances of each class
    a = A()
    b = B()
    c = C()
    d = D()
    
    print("Calling show() from each class:")
    print("\nClass A:")
    a.show()
    
    print("\nClass B:")
    b.show()
    
    print("\nClass C:")
    c.show()
    
    print("\nClass D (Diamond Inheritance):")
    d.show()
    
    # Display the Method Resolution Order (MRO) for class D
    print("\nMethod Resolution Order (MRO) for class D:")
    print(D.__mro__)
