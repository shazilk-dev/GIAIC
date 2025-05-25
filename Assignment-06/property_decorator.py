class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    
    @property
    def price(self):
        print("Getting price")
        return self._price
    
    @price.setter
    def price(self, value):
        print("Setting price")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        print("Deleting price")
        self._price = 0


if __name__ == "__main__":
    # Create a product
    product = Product("Laptop", 999.99)
    
    # Get price using the property
    print(f"Product: {product.name}")
    print(f"Price: ${product.price}")
    
    # Set price using the property
    product.price = 1299.99
    print(f"Updated price: ${product.price}")
    
    # Try setting an invalid price
    try:
        product.price = -10
    except ValueError as e:
        print(f"Error: {e}")
    
    # Delete price
    del product.price
    print(f"Price after deletion: ${product.price}")
    
    # We're still accessing the protected attribute via properties
    print(f"Direct access to protected attribute: ${product._price}")
