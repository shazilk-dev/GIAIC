class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


if __name__ == "__main__":
    print(f"5 + 3 = {MathUtils.add(5, 3)}")
    print(f"10 + 20 = {MathUtils.add(10, 20)}")
    
    math_instance = MathUtils()
    print(f"7 + 8 = {math_instance.add(7, 8)}")
