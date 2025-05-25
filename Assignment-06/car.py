class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"The {self.brand} car is starting...")


if __name__ == "__main__":
    my_car = Car("Toyota")
    
    print(f"Car brand: {my_car.brand}")
    
    my_car.brand = "Honda"
    print(f"New car brand: {my_car.brand}")
    
    my_car.start()
