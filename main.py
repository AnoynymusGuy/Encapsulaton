class Computer:
    def __init__(self):
        self._max_price = 100000

    def get_max_price(self):
        return self._max_price

    def set_max_price(self, price):
        self._max_price = price

Asus = Computer()
print(Asus.get_max_price())

Asus.set_max_price(99999)
print(Asus.get_max_price())