
class Product:
    def __init__(self, name =None,model=None,description=None,price=None, quantity=None):  #
        self.name = name  # שם המוצר
        self.model = model # דגם
        self.description = description  # תיאור המוצר
        self.price = price  # מחיר המוצר
        self.quantity = quantity  # הכמות המוצר
        self.rate = []

    def get_key_name(self):
        return self.name.replace(" ", "").translate(str.maketrans("", "", ".,!?;:"))
    def get_model_name(self):
        return self.model.replace(" ", "").translate(str.maketrans("", "", ".,!?;:"))
    def buy_product(self, many):  # הוצאת כמות מוצרים מהמלאי
        if self.available(many):
            self.quantity -= many
            return True
        else:
            return False

    def update_price(self, new_price):  # שינוי מחיר
        self.price = new_price

    def change_quantity(self, new_quantity):  # שינוי המלאי לפי מלאי חדש
        self.quantity = new_quantity

    def get_price(self, much):  # לראות רק את המחיר
        return self.price * much

    def get_quantity(self):  # לראות רק את הכמות של המוצר
        return self.quantity
    def add_quantity(self, quantity):
        self.quantity += quantity
    def available(self, how_many):  # בדיקת זמינות של מוצר מסוים
        return self.quantity >= how_many
    def add_review(self,review):
        self.rate.append(review)
        self.review_count+=1
        return "Thank you for your opinion"


    def review(self):
        review = '=================Rating=====================\n'
        if self.rate is not None and len(self.rate)>0:
            for rate in self.rate:
                review+=rate

        else:
            review +='There are no reviews yet'

        return review
    def __str__(self):
        return f" ======================================\nName: {self.name}\n Model: {self.model}\n Description: {self.description}\n \n Price: {self.price}₪\n{self.review()}"
