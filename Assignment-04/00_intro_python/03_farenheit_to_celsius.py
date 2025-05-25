
def main():
    temp_in_farenheit: float = float(input("Enter the temperature in Farenheit: "))

    temp_in_celsius: float = (temp_in_farenheit - 32) * 5.0/9.0

    print(f"Temperature: {temp_in_farenheit}F = {temp_in_celsius}C")


if __name__ == "__main__":
    main()