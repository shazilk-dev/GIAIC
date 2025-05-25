class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor


if __name__ == "__main__":
    # Create a Multiplier instance
    double = Multiplier(2)
    triple = Multiplier(3)
    
    # Check if instances are callable
    print(f"Is double callable? {callable(double)}")
    print(f"Is triple callable? {callable(triple)}")
    
    # Call the instances as if they were functions
    print(f"double(5) = {double(5)}")
    print(f"double(10) = {double(10)}")
    print(f"triple(5) = {triple(5)}")
    
    # Create a multiplier with a different factor
    times_ten = Multiplier(10)
    print(f"times_ten(7) = {times_ten(7)}")
    
    # Compare with a regular function
    def multiply_by_five(x):
        return x * 5
    
    print(f"Is multiply_by_five callable? {callable(multiply_by_five)}")
    print(f"multiply_by_five(4) = {multiply_by_five(4)}")
    
    # Non-callable example
    number = 42
    print(f"Is number callable? {callable(number)}")
    # This would raise TypeError: number is not callable
    # number(5)
