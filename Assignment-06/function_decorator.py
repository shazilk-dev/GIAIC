def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is being called")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} has finished execution")
        return result
    return wrapper


@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Greeting to {name} was sent"


@log_function_call
def calculate_sum(a, b):
    result = a + b
    print(f"Sum: {result}")
    return result


if __name__ == "__main__":
    # Call the decorated functions
    result1 = say_hello("John")
    print(f"Return value: {result1}")
    
    print("\n" + "-" * 40 + "\n")
    
    result2 = calculate_sum(5, 10)
    print(f"Return value: {result2}")
