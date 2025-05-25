class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. Got: {age}")


def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    return f"Age verified: {age} is valid"


if __name__ == "__main__":
    # Test the function with valid age
    try:
        result = check_age(25)
        print(result)
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with invalid ages
    ages = [15, 17, 18, 21]
    for age in ages:
        try:
            result = check_age(age)
            print(result)
        except InvalidAgeError as e:
            print(f"Error for age {e.age}: {e.message}")
    
    # Example of handling different exception types
    print("\nAttempting to check age with invalid input:")
    try:
        user_input = "twenty"
        age = int(user_input)
        result = check_age(age)
        print(result)
    except InvalidAgeError as e:
        print(f"Age validation error: {e}")
    except ValueError:
        print(f"Invalid input: '{user_input}' is not a valid number")
