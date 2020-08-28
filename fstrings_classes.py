class A(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sing(self):
        print(f"Hello, {self.name}. You are {self.age}.")
p1=A("Tom", 30)
f"{p1}"

