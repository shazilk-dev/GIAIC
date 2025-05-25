class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5/9


if __name__ == "__main__":
    # Using static methods without creating an instance
    celsius = 25
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit}°F")
    
    fahrenheit = 98.6
    celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
    
    # Can also be called from an instance (though not typical)
    converter = TemperatureConverter()
    print(f"100°C = {converter.celsius_to_fahrenheit(100)}°F")
