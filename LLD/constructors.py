class Person:
    def __init__(self, *args):
        if len(args) == 2:
            self.name = args[0]
            self.age = args[1]
        elif len(args) == 1:
            self.name = args[0]
        else:
            raise IndexError("Invalid number of arguments")

p = Person("John",36,35)
print(p.name)
# print(p.age)