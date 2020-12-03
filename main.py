class Order:
    order_items = None

    def __init__(self):
        return

    def add_order_item(self, order_item):
        return

    def remove_order_item(self, order_item):
        return

    def edit_order_item(self, order_item):
        return

    def place_order(self):
        return

    def save_order(selfself):
        order_saved_success_from_server = None
        return order_saved_success_from_server

    def re_order(self, order_number):
        return


class Payment:
    def __init__(self, last_four_digits, card, ):
        self.last_four_digits = self.encrypt_last_four_digits_of_payment_card(last_four_digits)
        self.is_debit = self.detect_card_type(card) == 'Debit',
        self.is_credit = self.detect_card_type(card) == 'Credit',
        self.payment_history


    def payment_history(self):
        return None


    def detect_card_type(self, card):
        return


    def encrypt_last_four_digits_of_payment_card(self, digits):
        return None


class Customer:
    def __init__(self, first_name, last_name, email, password, recovery_question, recovery_answer):
        self.firstName = first_name
        self.lastName = last_name
        self.email = email
        self.password = password
        self.recoveryQuestion = recovery_question
        self.recoveryAnswer = recovery_answer
        self.is_logged_in = None
        self.is_user_guest = None
        self.order = Order()
        self.payment = Payment()
        self.is_created_successful = None

    def is_logged_in(self):
        return None


class Authentication:
    users_in_system = None
    logged_in_users = None

    def login(self, customer_to_login):
        return

    def logout(self, customer):
        return

    @staticmethod
    def does_email_exist(email):
        return None

    @staticmethod
    def does_user_know_recovery_answer(customer, recovery_answer):
        return


class MenuItem:
    def __init__(self, name, item_type, image, price, options):
        self.name = name
        self.item_type = item_type
        self.image = image
        self.price = price
        self.options = options


class Menu:
    menu_items = None

    def add_item_to_menu(self, menu_items):
        return


    def remove_item_to_menu(self, menu_items):
        return


# Requirement: The customer will be able to login to the system
def test_does_customer_email_exist():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    assert authentication.login(customer) is True,\
        'The customers email should exist when logging in'


def test_does_customer_email_and_password_match():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    authentication = Authentication()
    assert authentication.does_email_exist(customer.email) is True , \
        'The customers email should exist when logging in'


def test_is_customer_already_logged_in():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert customer.is_logged_in is True | customer.is_user_guest is True, \
        'The customers email should exist when logging in'


def test_is_customer_logged_into_an_account():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert customer.is_logged_in() is True, \
        'The customers email should exist when logging in'


def test_is_customer_logged_in_as_a_guest():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert len(customer.email) == 0, \
        'The customers email should not exist when logging in as a guest'


def test_customer_should_not_be_logged_in():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    assert customer.is_logged_in is False, 'The customer should not be logged in if they have not logged in yet'


def test_customer_should_be_logged_in_after_logging_in():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    authentication.login(customer)
    assert customer.is_logged_in is True, 'The customer should be able to login if they have an account'


# Requirement: The customer will be able to manage their account
def test_user_should_know_recover_answer_for_account():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    assert authentication.does_user_know_recovery_answer(customer, 'Adam Sandler') is True,\
        'The customer should be able to change the password if they know the answer to the security question'


def test_user_should_not_recover_answer_for_account():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    assert authentication.does_user_know_recovery_answer(customer, 'Tyler Perry') is False,\
        'The customer should not be able to change password for the account if he / she does not know the security answer'


# Requirement: The customer will be able to view all the items on the menu
def test_customer_should_be_able_to_view_menu_as_authenticated_user_with_account():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    authentication.login(customer)
    test_beer_menu = []

    if customer.is_logged_in:
        test_beer_menu = beer_menu

    assert test_beer_menu == beer_menu, \
        'The customer should be able to view the menu if they are logged in with an account'


def test_customer_should_be_able_to_view_menu_as_guest():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    authentication.login(customer)
    test_beer_menu = []

    if customer.is_user_guest:
        test_beer_menu = beer_menu

    assert test_beer_menu == beer_menu, 'The customer should be able to view the menu as a guest'


def test_customer_should_not_be_able_to_view_menu_if_not_authenticated():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    authentication.login(customer)
    test_beer_menu = []

    if customer.is_logged_in == False & customer.is_user_guest == False:
        test_beer_menu = beer_menu

    assert test_beer_menu == beer_menu, \
        'The customer should be able to view the menu if they are logged in with an account'


# The customer will be able to select one or more options to customize an item.
def test_customer_should_be_able_to_add_select_one_or_more_options():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')

    assert len(customer.order.order_items) == 1, 'The customer be able to customize their order'


def test_customer_should_be_able_to_not_add_an_option_options():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, []))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, []))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, []))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    assert len(customer.order.order_items) == 1, 'The customer be able to customize their order'


# The customer will be able to add an item to their current order.
def test_customer_should_be_able_to_add_one_item_to_their_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    customer.order.add_order_item(beer_menu.menu_items[0])

    assert len(customer.order.order_items) == 1, 'The customer should be able to add only 1 item to their order'


def test_customer_should_be_able_to_add_items_to_their_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    customer.order.order_items = []
    customer.order.add_order_item(beer_menu.menu_items[0])
    customer.order.add_order_item(beer_menu.menu_items[2])
    customer.order.add_order_item(beer_menu.menu_items[1])
    assert len(customer.order.order_items) == 3, 'The customer should be able to add multiple items to their order'


# The customer will be able to review their current order.
def test_customer_order_should_start_out_empty():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')

    assert len(customer.order.order_items) == 0, 'The customers order should start out empty'


def test_customer_order_price_should_start_out_at_zero():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    assert len(customer.order.price) == 0, 'The customers order should start out empty'


def test_customer_should_be_able_to_view_their_order():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    authentication = Authentication()
    is_menu_allowed_to_be_viewed = False

    if customer.is_logged_in | customer.is_user_guest:
        is_menu_allowed_to_be_viewed = True

    assert is_menu_allowed_to_be_viewed == True, 'The customer should be able view their order if they are logged in'


# The customer will be able to remove an item/remove all items from their current order.
def test_customer_should_not_be_able_to_remove_item_from_their_order_if_their_are_no_orders():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    customer.order.remove_order_item(beer_menu.menu_items[0])
    assert len(customer.order.order_items) == 0, 'The customer should be able to remove an item from their order'


def test_customer_should_be_able_to_remove_item_from_their_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    customer.order.add_order_item(beer_menu.menu_items[0])
    customer.order.remove_order_item(beer_menu.menu_items[0])
    assert len(customer.order.order_items) == 0, 'The customer should be able to remove an item from their order'


# The customer will be able to modify their order
def test_customer_should_be_able_to_add_order_to_their_cart():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    customer.order.add_order_item(beer_menu.menu_items[0])
    previous_beer_option_type = customer.order.order_items[0].item_type
    new_beer_item = beer_menu.menu_items[0]
    new_beer_item.item_type = 'draft'
    customer.order.edit_order_item(new_beer_item)

    assert previous_beer_option_type != new_beer_item.item_type, 'The customer should be able to remove an item from their order'


# The customer will be able to see total currency to be paid, be given payment options, process payment order.
def test_customer_order_total_should_start_at_0():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')

    assert customer.order.total_price == 0, 'The customers order total price should start at 0 dollars'


def test_customer_order_should_increase_when_items_are_added_to_the_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    customer.order.add_order_item(beer_menu.menu_items[0])
    assert customer.order.total_price == 2,\
        'The customers order total price should increase when items are added to their order'


def test_customer_order_should_decrease_when_items_are_added_to_the_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    customer.order.add_order_item(beer_menu.menu_items[0])
    customer.order.add_order_item(beer_menu.menu_items[2])
    customer.order.add_order_item(beer_menu.menu_items[1])
    customer.order.remove_order_item(beer_menu.menu_items[0])
    assert customer.order.total_price == 4,\
        'The customers order total price should increase when items are added to their order'


def test_customer_order_should_go_into_the_negative():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    customer.order.remove_order_item(beer_menu.menu_items[0])
    assert customer.order.total_price == 0,\
        'The customers order total price should increase when items are added to their order'


# The customer will be able to place the order.
def test_customer_order_price_and_items_should_be_cleared_after_placing_their_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('bottle', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    beer_menu.add_item_to_menu(MenuItem('can', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    customer.order.add_order_item(beer_menu.menu_items[0])
    customer.order.add_order_item(beer_menu.menu_items[2])
    customer.order.place_order()
    assert customer.order.total_price == 0, 'The customers price should go back to 0 after their order is placed'
    assert len(customer.order.order_items) == 0, 'The customers order should be emptied after the order is placed'


def test_customer_should_be_able_to_place_their_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity', 'Lindsey Lohan')
    customer.order.add_order_item(beer_menu.menu_items[0])
    customer.order.place_order()
    assert customer.order.isPlaced == True, 'The customers should be able to place their order'


def test_customer_should_not_be_able_to_place_their_order_if_their_are_no_items_in_their_order():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert customer.order.place_order(), 'The customer should not be able place their order if there are no items in their order'


def test_customer_should_be_able_to_save_their_order():
    beer_menu = Menu()
    beer_menu.add_item_to_menu(MenuItem('tap', 'drink', None, 2, ['IPA', 'Sour', 'Port', 'Lager', 'Ale']))
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    customer.order.add_order_item(beer_menu.menu_items[0])

    assert customer.order.save_order(), 'The customer should be able to save their order after ordering'


def test_customer_should_not_be_able_to_save_their_order_until_it_is_placed():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert customer.order.save_order(), 'The customer should not be able to save their order until the order is placed'


# The customer will be allowed to re-order the save order
def test_customer_should_be_allowed_to_re_order_existing_order():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert customer.order.re_order(1), 'The customer should be able to re-order'


def test_customer_should_not_be_allowed_to_re_order_out_of_their_orders_saverd():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert customer.order.re_order(10), 'The customer should not be allowed to use an order id that does not exist'


def test_customer_should_not_be_allowed_to_use_an_order_id_in_the_negative():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')
    assert customer.order.re_order(-24), 'The customer should be able to re-order using a negative order item id'


# The customer will receive confirmation in the form of an order number
def test_customer_should_recieve_confirmation_if_order_is_successful():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    order_confirmation = customer.order.place_order()
    assert order_confirmation == True, 'The customer recieve confirmation if their order is successfull'


def test_customer_should_not_recieve_confirmation_if_order_was_ussuccessful():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    order_confirmation = customer.order.place_order()
    assert order_confirmation == False, 'The customer should not receive a successful confirmation if order was not successful'


# The last 4 digits of a users save credit or debit card should not be displayed in the app to prevent potential hijackers
# from being able to get a users complete banking card number
def test_customers_last_4_digits_of_payment_method_should_be_saved():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    customer.order.place_order()
    assert len(customer.payment.last_four_digits) == 4, 'The last four digits of the customers payment card should be saved'


def test_customers_payment_should_know_if_it_is_debit():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    customer.order.place_order()

    assert customer.payment.is_debit == True, 'The customers payment card should be debit'


def test_customers_payment_should_know_if_it_is_Credit():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    customer.order.place_order()
    assert len(customer.payment.is_credit) == True, 'The customers payment card should be credit'


# Security questions must be created during account creation to ensure security of a user’s account before a user can reset their password.
def test_customers_must_enter_security_question_and_answer_to_create_an_account():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    assert len(customer.is_created_successful) == True, 'The customer must enter a security question and answer to create an account'


def test_customers_should_not_be_able_to_create_an_account_if_security_question_or_answer_is_not_provided():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    assert len(customer.is_created_successful) == True, 'The customer should not be able to create an account if the security question or answer is not provided'


# Users debit and credit card can be stored however information should be encrypted to help secure the users information.
def customer_last_four_digits_of_payment_card_should_be_encrypted():
    customer = Customer('Pam', 'Blart', 'blartPam@gmail.com', 'blarts#awesome!', 'Favourite celebrity',
                        'Lindsey Lohan')

    assert len(customer.payment.last_four_digits) == Payment.encrypt_last_four_digits_of_payment_card(4456),\
        'The custoemrs payment last four digits should be encrypted'
7