class SetGet:
    def __init__(self):
        self.name = None
        self.age = None
        self.address = None

    def set_name(self, name) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_age(self, age) -> None:
        self.age = age

    def get_age(self) -> int:
        return self.age

    def set_address(self,address) -> None:
        self.address = address

    def get_address(self) -> str:
        return self.address

str1 = SetGet()
str1.set_name("Bhanu Prakash")
print(str1.get_name())
print(str1.get_age())