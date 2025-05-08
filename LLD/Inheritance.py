from django.forms.utils import pretty_name


class Parent():
    def __init__(self):
        print("Parent constructor")
        self.eyes = 2
    def speak(self):
        print("parent Speak")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")

    def speak(self):
        print("child Speak")


c= Child()
print(c.eyes)
