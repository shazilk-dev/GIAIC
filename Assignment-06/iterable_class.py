class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


if __name__ == "__main__":
    # Create a Countdown object
    countdown = Countdown(5)
    
    # Use it in a for loop
    print("Countdown from 5:")
    for num in countdown:
        print(num, end=" ")
    print("\nBlastoff!")
    
    # Use it in another for loop (need to get a fresh iterator)
    print("\nAnother countdown from 10:")
    for num in Countdown(10):
        print(num, end=" ")
    print("\nBlastoff!")
    
    # Convert to a list
    countdown_list = list(Countdown(3))
    print(f"\nCountdown as a list: {countdown_list}")
    
    # Manual iteration using next()
    print("\nManual iteration:")
    manual_countdown = iter(Countdown(3))
    try:
        while True:
            value = next(manual_countdown)
            print(value, end=" ")
    except StopIteration:
        print("\nManual countdown complete")
