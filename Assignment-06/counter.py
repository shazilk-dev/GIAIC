class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")
    
    @classmethod
    def reset_count(cls):
        cls.count = 0
        print("Counter has been reset to 0")


if __name__ == "__main__":
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    
    Counter.display_count()
    
    c4 = Counter()
    c5 = Counter()
    
    Counter.display_count()
