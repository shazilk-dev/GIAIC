class Engine:
    def __init__(self, type, horsepower):
        self.type = type
        self.horsepower = horsepower
    
    def start(self):
        return f"{self.type} engine with {self.horsepower} HP started"
    
    def stop(self):
        return f"{self.type} engine stopped"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has-a Engine
    
    def start_engine(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop_engine(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"
    
    def display_info(self):
        return f"Car: {self.make} {self.model}, Engine: {self.engine.type} ({self.engine.horsepower} HP)"


if __name__ == "__main__":
    # Create an engine
    v8_engine = Engine("V8", 450)
    
    # Create a car with the engine
    sports_car = Car("Ferrari", "F8", v8_engine)
    
    # Access engine methods through the car
    print(sports_car.display_info())
    print(sports_car.start_engine())
    print(sports_car.stop_engine())
    
    # Create another car with a different engine
    electric_engine = Engine("Electric", 670)
    electric_car = Car("Tesla", "Model S", electric_engine)
    
    print("\n" + "-" * 40 + "\n")
    print(electric_car.display_info())
    print(electric_car.start_engine())
    print(electric_car.stop_engine())
