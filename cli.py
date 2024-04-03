from Store.store import Store
from Store.order import Order
from Store.product import Product
from Store.user import User
class StoreCLI:
    def __init__(self):
        self.store = Store()

    def log_in(self):
        user_id = input("Enter User ID")
        if user_id in self.store.users:
            user = self.store.users[user_id]
            password = input("Enter Password")
            user = user.login(password)
            return user

        else:
            print("The user does not exist in the system, please register")

    def register(self):
        user_id = input("Enter User ID")
        full_name = input("Enter your Full name")
        pass_word = input("Enter your Password")
        new_user = User(user_id,full_name,pass_word)
        if self.store.add_user(new_user):
            return new_user
        else:
            new_user = User("error")
            print("\nPlease try again")
            return new_user


    def display_user(self):
        print("1. Log in")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter your choice: ")
        return choice


    def display_order(self):
        print("1.Add Item")
        print("2.Return To main menu")
        choice = input("Enter your choice: ")
        return choice








    def display_menu(self):
            print("\nElectronic store Management System")
            print("1. Add Product")
            print("2. Add User")
            print("3. Place Order")
            print("4. Remove Product")
            print("5. List Product")
            print("6. List Orders")
            print("7. Reporting")
            print("7. Exit")
            choice = input("Enter your choice: ")
            return choice

    def add_item(self,order):
        name = input("Enter Product name")
        if name in self.store.collection:
            print(self.store.collection[name])
            how_much = input("Enter a quantity of the following product")
            if how_much.isdigit():
                how_much = int(how_much)
                self.store.add_item_order(self.store.collection[name],how_much,order)
        else:
            print("The product you entered does not exist in the store")

    def add_product(self):
        name = input("Enter Product Name: ")
        description = input("Enter Description: ")
        price = input("Enter Price")
        quantity = input("Enter Quantity")
        if price.isdigit() and quantity.isdigit():
            price = float(price)
            quantity = int(quantity)
            product = Product(name,description,price,quantity)
            self.store.add_product(product)
        else:
            print("Price and Quantity must be a digit")

    def place_order(self):
        customer_name = input("Enter Customer Name: ")
        new_order = Order(customer_name)
        while True:
            choice = self.display_order()
            if choice == '1':
                self.add_item(new_order)
            elif choice =='2':
                break
        if new_order.product_dict != None:
            self.store.place_order(new_order)
            print(new_order)

    def remove_product(self):
       name = ("Input Product Name: ")
       if name in self.store.collection:
            print(f"{self.store.collection[name]} has been removed")
            self.store.remove(self.store.collection[name])
    def list_products(self):
        print(self.store.list_products())

    def orders(self):
        for order_number in self.store.list_orders():
            print(order_number)




    def run(self):
        user = User()
        while user.online == False:
            selc = self.display_user()
            if selc == '1':
                user = self.log_in()
            elif selc == '2':
                user = self.register()
                if user.user_id is not None:
                    user.online = True
            elif selc == '3':
                break
            else:
                print("Invalid choice. Please try again.")

        while True:

            choice = self.display_menu()

            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.register()
            elif choice == '3':
                self.place_order()
            elif choice == '4':
                self.remove_product()
            elif choice == '5':
                self.list_products()
            elif choice == '6':
                self.orders()
            elif choice == '7':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cli = StoreCLI()
    cli.run()