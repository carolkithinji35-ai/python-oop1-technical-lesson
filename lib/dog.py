# Dog model goes here
class Dog:
    def __init__(self, name,  breed, age, last_checkup=None):
        self.name = name
        self.age = age
        self.breed = breed
        self.last_checkup = last_checkup

    def checkup(self, date):
        self.last_checkup = date
        print(f"{self.name} was last checked on {date}")

    def birthday_celebration(self, gender):
        self.age += 1
        print(f"{gender} is turning {self.age}")

    def get_age(self):
        return self._age

    def set_age(self, value):
        if type(value) is int and 0 <= value:
            self._age = value
        else:
            print("Not valid age")
            
    age = property(get_age, set_age)


fido = Dog("Fido", "Husky", 4)

print(fido.name)
print(fido.age)
print(fido.breed)
fido.last_checkup = "03/02/2023"
print(fido.last_checkup)
fido.checkup("03/02/2023")
fido.birthday_celebration("He")

clifford = Dog("Clifford", "Big Red Dog", 10)

print(clifford.name)
print(clifford.age)
print(clifford.breed)
clifford.last_checkup = "01/01/2023"
print(clifford.last_checkup)
clifford.checkup("01/01/2023")
clifford.birthday_celebration("He")
