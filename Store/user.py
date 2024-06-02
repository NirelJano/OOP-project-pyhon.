from Store.payment import Payment
class User:
    def __init__(self, user_id=None, user_full_name=None, password=None, online=0, address=None, payment=None):
        self.__user_id = user_id
        self.__user_full_name = user_full_name
        self.__password = password
        self.__online = online
        self.__address = address
        if payment is not None:
            self.payment = payment
        else:
            self.payment = Payment()


    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id):
        self.__user_id = user_id

    @property
    def user_full_name(self):
        return self.__user_full_name

    @user_full_name.setter
    def user_full_name(self, user_full_name):
        self.__user_full_name = user_full_name

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def online(self):
        return self.__online

    @online.setter
    def online(self, online):
       self.__online = online

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address



    def login(self, entered_password):
        if self.password == entered_password:
            self.online = 1
            return True
        else:
            return False

    def logout(self):
        self.online = 0
        return 'Logged out successfully.'

    def change_user_password(self, new_password):
        self.password = new_password
        return True

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'user_full_name': self.user_full_name,
            'password': self.__password,
            'address': self.__address,
            'payment': self.payment.payment_to_dict_user(),
            'user_type':'Admin'
        }
    def __eq__(self, other):
        if self.user_id == other.user_id and self.user_full_name == other.user_full_name and self.password == other.password:
            return True


    def __str__(self):
        return f"User: {self.user_full_name}\nID: {self.user_id}"
