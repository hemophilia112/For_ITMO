class Product:
    def __init__(self, name,price, quantity):
        self.name = name
        self._price = price
        self.quantity = quantity

    def get_total_price(self):
        summ_price = self.price*self.quantity
        return summ_price


    def sell(self, quantity):
        if quantity > 0:
            if quantity > self.quantity:
                return f"Недостаточно товара на складе! Остаток не изменился {self.quantity}"
            else:
                self.quantity = self.quantity - quantity
                return f"Успех. На складе осталось: {self.quantity}шт. "
        else:
            return f"Некорректный ввод. Остаток прежний {self.quantity} шт "


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if value > 0:
            self._price = value
        return f"Успех. Цена {self.name} изменилась на {self._price}"


prod1 = Product("Дрель", 3500, 4)
prod2 = Product("Шуруповерт", 5000, 2)

#tests
# print(f"{prod1.name} - Общая стоимость: {prod1.get_total_price()}")
# print(f"{prod2.name} - Общая стоимость: {prod2.get_total_price()}")
#
# print(prod1.sell(-4))
# print(f"{prod1.name} - Общая стоимость: {prod1.get_total_price()}")
#
# print(prod1.price)
# prod1.price = 4000
# print(prod1.price)
# prod1.price = -500
# print(prod1.price)
