"""
    Vending machine kata.
    Author: John Wheeler
    Date: 08/29/2017
"""

# Coins
PENNY = "PENNY"
NICKEL = "NICKEL"
DIME = "DIME"
QUARTER = "QUARTER"

# Products
COLA = "COLA"
CHIPS = "CHIPS"
CANDY = "CANDY"

class VendingMachine():
    """Represents a vending machine."""

    # Coins that the vending machine are able to accept and their value.
    VALID_COINS = {NICKEL : 0.05, DIME : 0.10, QUARTER : 0.25}

    # Products that are in the vending machine.
    PRODUCTS = {COLA : 1.00, CHIPS : 0.50, CANDY : 0.65}

    def __init__(self):
        # Current coin inventory. Coin and quantity.
        self.coin_inventory = {}

        # Coin return with number of coins.
        self.coin_return = {}

        # Monetary amount inserted by the customer.
        self.current_amount = 0.0

        # Vending machine display unit.
        self.display = ""

        # Product dispense bin.
        self.product_dispense_bin = ""

        # Current product inventory. Product name and quantity.
        self.product_inventory = {}

        # Acceptable coins and the number entered by the customer.
        # Coin and quantity.
        self.inserted_coins = {}

        for coin in self.VALID_COINS:
            self.coin_inventory[coin] = 0
            self.inserted_coins[coin] = 0

        for product in self.PRODUCTS:
            self.product_inventory[product] = 0

    def dispense_product(self, product):
        """
        Dispense the product once the user has entered enough money.
        Coins should be transferred into the coin inventory and the product
        moved into the product dispense bin for the customer to take.
        """
        if self.current_amount < self.PRODUCTS[product]:
            return

        self.product_dispense_bin = product
        for coin in self.inserted_coins:
            if self.inserted_coins[coin] > 0:
                self.coin_inventory[coin] = self.inserted_coins[coin]
                self.inserted_coins[coin] = 0

        self.current_amount -= self.PRODUCTS[product]
        self.product_inventory[product] -= 1

    def check_display(self):
        if self.current_amount > 0.0:
            display = ("$%.2f" % self.current_amount)
        else:
            display = "INSERT COIN"

        return display

    def exact_change_only(self):
        """Return true if exact change is needed."""
        min_coin = min(self.VALID_COINS.values())
        max_coin = max(self.VALID_COINS.values())

        coin_value_delta = round(max_coin - min_coin, 2)

        offset = min_coin
        while offset <= coin_value_delta:
            can_make_change = self.make_change(round(offset, 2), return_coin=False)
            if can_make_change is False:
                return True
            offset += min_coin

        return False

    def insert_coin(self, coin):
        """
        Insert a coin into the vending machine.
        Accepted coins will be placed into the inserted coins bin and the
        value of the coin will be added to the current amount.
        Rejected coins will be placed in the coin return bin.
        """
        if self.is_valid_coin(coin):
            self.current_amount += self.VALID_COINS[coin]
            self.inserted_coins[coin] += 1
        else:
            # Place rejected coin in the coin return bin.
            self.return_coin(coin, 1)

    def is_machine_sold_out(self):
        """Returns True if the vending machine is sold out of products."""
        for product in self.product_inventory:
            if self.product_inventory[product] > 0:
                return False

        return True

    def is_valid_coin(self, coin):
        """Returns True if the coin is a valid and acceptable coin."""
        if coin in self.VALID_COINS:
            return True

        return False

    def make_change(self, amount, return_coin=True):
        """Make change to return to the customer for the amount of they overpaid."""
        # Order dictionary in the descending direction by coin value.
        coin_dict_desc = sorted(self.VALID_COINS.items(), key=lambda x: x[1], reverse=True)
        for coin_name, coin_value in coin_dict_desc:
            while coin_value <= round(amount, 2) and self.coin_inventory[coin_name] > 0:
                amount -= coin_value
                if return_coin:
                    self.coin_inventory[coin_name] -= 1
                    self.return_coin(coin_name, 1)

        if round(amount, 2) == 0.0:
            return True
        else:
            return False

    def return_coin(self, coin, quantity):
        """Place the returned coins in the return coin bin."""
        if coin in self.coin_return:
            self.coin_return[coin] += quantity
        else:
            self.coin_return[coin] = quantity

    def return_inserted_coins(self):
        """Return the inserted coins to the customer."""
        for coin in self.inserted_coins:
            if self.inserted_coins[coin] > 0:
                # Place coin in the return coin bin.
                self.return_coin(coin, self.inserted_coins[coin])

                self.current_amount -= (self.VALID_COINS[coin] * self.inserted_coins[coin])

                # Remove the coin from the inserted coins bin.
                self.inserted_coins[coin] = 0

    def select_cola(self):
        """Select cola from the vending machine."""
        self.dispense_product(COLA)

    def select_chips(self):
        """Select chips from the vending machine."""
        self.dispense_product(CHIPS)

    def select_candy(self):
        """Select candy from the vending machine."""
        self.dispense_product(CANDY)
