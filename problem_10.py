class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Car Details:\n Brand: {self.brand}\n Model: {self.model}\n Year: {self.year}")

obj = Car("Honda", "old_model", 2019)
obj.display_info()

