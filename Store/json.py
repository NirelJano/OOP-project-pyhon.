import json
import logging
from Store.order import Order
from Store.product import Product
from Store.user import User
from Store.client import Client
from Store.payment import Payment
from Store.reporting import Reporting
from Store.tv import Tv
from Store.phone import Phone
from Store.computer import Computer
from Store.rating import Rating

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - LEVEL - %(message)s')

class DataManager:
    @staticmethod
    def load_data(filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            logging.warning(f"File {filename} not found.")
            return []
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from file {filename}.")
            return []

    @staticmethod
    def save_data(data, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info(f"Data successfully saved to {filename}.")
        except IOError as e:
            logging.error(f"Error saving data to file {filename}: {e}")

    @staticmethod
    def load_orders(users: dict):
        orders = {}
        orders_data = DataManager.load_data('Store/orders_logg.JSON')
        for order_data in orders_data:
            customer = users.get(order_data['customer_id'])
            if customer:
                order = Order(
                    order_number=order_data['order_number'],
                    customer=customer,
                    product_dict=order_data['product_dict'],
                )
                order.status = order_data['status']
                orders[order.order_number] = order
        logging.info(f"Orders loaded from {'Store/orders_logg.JSON'}.")
        return orders

    @staticmethod
    def save_orders(orders):
        orders_data = [
            {
                'order_number': order.get_order_number(),
                'customer_id': order.get_customer().user_id,
                'product_dict': order.get_product_dict(),
                'status': order.get_status()
            } for order in orders.values()
        ]
        DataManager.save_data(orders_data, 'Store/orders_logg.JSON')

    @staticmethod
    def load_products():
        products_data = DataManager.load_data('Store/products_logg.JSON')
        collection = {}
        for prod_data in products_data:
            product_type = prod_data.get('product_type')
            if product_type == 'Tv':
                product = Tv(
                    name=prod_data.get('name'),
                    model=prod_data.get('model'),
                    description=prod_data.get('description'),
                    price=prod_data.get('price'),
                    quantity=prod_data.get('quantity'),
                    size=prod_data.get('size'),
                    type=prod_data.get('type')
                )
            elif product_type == 'Computer':
                product = Computer(
                    name=prod_data.get('name'),
                    model=prod_data.get('model'),
                    description=prod_data.get('description'),
                    price=prod_data.get('price'),
                    quantity=prod_data.get('quantity'),
                    size=prod_data.get('size'),
                    storage=prod_data.get('storage'),
                    chip=prod_data.get('chip')
                )
            elif product_type == 'Phone':
                product = Phone(
                    name=prod_data.get('name'),
                    model=prod_data.get('model'),
                    description=prod_data.get('description'),
                    price=prod_data.get('price'),
                    quantity=prod_data.get('quantity'),
                    size=prod_data.get('size'),
                    storage=prod_data.get('storage')
                )
            else:
                product = Product(
                    name=prod_data.get('name'),
                    model=prod_data.get('model'),
                    description=prod_data.get('description'),
                    price=prod_data.get('price'),
                    quantity=prod_data.get('quantity'),
                    rate=prod_data.get('rate')
                )
            collection[product.get_key_name()] = product
        logging.info(f"Products loaded from {'Store/products_logg.JSON'}.")
        return collection

    @staticmethod
    def save_products(products):
        products_data = []
        for product in products.values():
            product_data = {
                'name': product.name,
                'product_type': product.__class__.__name__,
                'model': product.model,
                'description': product.description,
                'price': product.price,
                'quantity': product.quantity,
                'rate': getattr(product, 'rate', None)
            }
            if isinstance(product, Tv):
                product_data.update({
                    'size': product.size,
                    'type': product.type
                })
            elif isinstance(product, Computer):
                product_data.update({
                    'size': product.size,
                    'storage': product.storage,
                    'chip': product.chip
                })
            elif isinstance(product, Phone):
                product_data.update({
                    'size': product.size,
                    'storage': product.storage
                })
            products_data.append(product_data)
        DataManager.save_data(products_data, 'Store/products_logg.JSON')

    @staticmethod
    def load_users():
        users = {}
        users_data = DataManager.load_data('Store/users_logg.JSON')
        for user_data in users_data:
            user_type = user_data.get('type')
            if user_type == 'Admin':  # Adjusted type to match JSON
                user = User(
                    user_id=user_data['user_id'],
                    user_full_name=user_data['user_full_name'],  # Adjusted name to match JSON
                    password=user_data['password']
                )
            elif user_type == 'Client':
                user = Client(
                    user_id=user_data['user_id'],
                    user_full_name=user_data['user_full_name'],  # Adjusted full_name to match JSON
                    password=user_data['password'],
                    address=user_data.get('address'),
                    payment=user_data.get('payment'),
                    coupon=user_data.get('coupon')
                )
            else:
                logging.warning(f"Unknown user type: {user_type}")
                continue
            users[user.user_id] = user
        logging.info(f"Users loaded from {'Store/users_logg.JSON'}.")
        return users

    @staticmethod
    def save_users(users: dict):
        users_data = []
        for user in users.values():
            if isinstance(user, Client):
                user_data = {
                    'user_id': user.user_id,
                    'type': 'Client',
                    'user_full_name': user.full_name,  # Adjusted to match JSON
                    'password': user.password,
                    'address': user.address,
                    'payment': user.payment,
                    'coupon': user.coupon
                }
            else:  # Assuming the only other type is Admin
                user_data = {
                    'user_id': user.user_id,
                    'type': 'Admin',  # Adjusted type to match JSON
                    'user_full_name': user.user_full_name,  # Adjusted to match JSON
                    'password': user.password
                }
            users_data.append(user_data)
        DataManager.save_data(users_data, 'Store/users_logg.JSON')

    @staticmethod
    def load_reporting():
        reporting_data = DataManager.load_data('Store/reporting_logg.JSON')
        reporting = Reporting()
        if reporting_data:
            reporting.revenue = reporting_data['revenue']
            reporting.best_sell = reporting_data['best_sell']
            reporting.sold_products = reporting_data['sold_products']
            reporting.message = reporting_data['message']
            reporting.new_update = reporting_data['new_update']
        logging.info(f"Reporting data loaded from {'Store/reporting_logg.JSON'}.")
        return reporting

    @staticmethod
    def save_reporting(reporting, sales):
        reporting_data = {
            'revenue': reporting.revenue,
            'best_sell': reporting.best_sell,
            'sold_products': reporting.sold_products,
            'message': reporting.message,
            'new_update': reporting.new_update,
            'sales': sales
        }
        DataManager.save_data(reporting_data, 'Store/reporting_logg.JSON')

    @staticmethod
    def load_sales():
        sales_data = DataManager.load_data('Store/reporting_logg.JSON')
        sales = []
        if sales_data:
            sales = sales_data['sales']
        return sales
