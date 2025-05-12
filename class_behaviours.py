# methods or behaviors or functions
class Laptop:
    chargerType = "C-Type"

    def __init__(self):
        self.price = 34
        self.ram = 8

    def setPrice(self, price):
        # instance method
        self.price = price

    def getPrice(self):
        return self.price

    @classmethod  # this avoids passing class again to do this change
    # class method
    def changeChargerType(cls):
        cls.chargerType = "USB-C"
        print(f"Changed charger type {cls.chargerType}")

    @staticmethod
    def info():
        print(f"This is a static method without cls and self")


Dell = Laptop()

Dell.setPrice(20000)

print(Dell.getPrice())

# Laptop.changeChargerType(Laptop) this method should be done to prevent error if we dont use @classmethod
Laptop.changeChargerType()

Dell.info()
