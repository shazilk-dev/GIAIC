
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random


def guess_my_number():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            guess = int(input("Enter a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        if guess == secret_number:
            print(f"Congrats! The number was: {secret_number}")
            break
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        
        print() 

if __name__ == "__main__":
    guess_my_number()