# In this program we show an example of using dictionaries to keep track of information in a phonebook.

phonebook = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phonebook[name] = number
    print(f"Contact {name} added successfully!")

def lookup_contact():
    name = input("Enter name to lookup: ")
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"No contact found with the name {name}")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"No contact found with the name {name}")

def display_contacts():
    if phonebook:
        print("\nPhonebook Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")
    else:
        print("Phonebook is empty")

while True:
    print("\nPhonebook Menu:")
    print("1. Add a contact")
    print("2. Look up a contact")
    print("3. Delete a contact")
    print("4. Display all contacts")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        lookup_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("Exiting phonebook. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")