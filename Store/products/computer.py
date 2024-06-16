from Store.products.product import Product


class Computer(Product):
    def __init__(self, name, model, description, price, quantity, size=None, storage=None,
                 chip=None, rate=None):
        super().__init__(name, model, description, price, quantity, rate)
        self.size = size
        self.storage = storage
        self.chip = chip

    def product_to_dict(self):
        dict = {
            "size": self.size,
            "storage": self.storage,
            "chip": self.chip,
        }
        dict = {**super().product_to_dict(), **dict}
        dict["product_type"] = "Computer"
        return dict

    def product_type(self):
        return "COMPUTER"

    def __str__(self):
        return f"======================================\n Name: {self.name}\n Model:{self.model}   |  Storge: {self.storage} \n Chip: {self.chip}\n display size: {self.size}-Inch \n Description: {self.description} \n {self.get_price_in_user_currency()}\n {self.rate}"