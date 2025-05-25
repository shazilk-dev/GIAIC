# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
# The formula for converting feet to inches is:
# inches = feet * 12

def main():
    feet = int(input("Enter number of feet: "))
    inches = feet * 12

    print(f'{feet} feet = {inches} inches')


if __name__ == "__main__":
    main()