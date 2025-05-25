class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Constructor: Logger object '{self.name}' created")
    
    def log(self, message):
        print(f"[{self.name}] {message}")
    
    def __del__(self):
        print(f"Destructor: Logger object '{self.name}' destroyed")


if __name__ == "__main__":
    print("Creating first logger")
    logger1 = Logger("SystemLog")
    logger1.log("System started")
    
    print("\nCreating second logger")
    logger2 = Logger("UserLog")
    logger2.log("User logged in")
    
    print("\nDeleting first logger")
    del logger1
    
    print("\nProgram ending - second logger will be destroyed automatically")
