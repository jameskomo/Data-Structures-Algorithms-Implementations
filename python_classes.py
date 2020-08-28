class Car:
    models="Toyota"
    def __init__(self, color, mileage):
        self.color=color 
        self.mileage=mileage

    def __repr__(self):
        return f"The {self.color} has {self.mileage} miles"

    # INSTANCE METHOD
    def description(self):
        return f"I am a {self.color} Car"

    # CLASS METHOD
    @classmethod
    def car_model(cls):
        return f"The model is {cls.models}"

    # STATIC METHOD
    @staticmethod
    def yom(year):
        return f"The year of manufacture is {year}"
    @staticmethod
    def split_string(string):
        name, age, status = string.split("-")
        print(f"{name}, {age} and {status}")

blue_car=Car("blue", 20000)
red_car=Car("red", 30000)
Car.split_string("komo-26-passed")




