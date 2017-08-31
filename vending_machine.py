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

        # Product dispense bin.
        self.product_dispense_bin = ""

        # Acceptable coins and the number entered by the customer.
        # Coin and quantity.
        self.inserted_coins = {}

        for key in self.VALID_COINS:
            self.coin_inventory[key] = 0
            self.inserted_coins[key] = 0

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

    def is_valid_coin(self, coin):
        """Returns True if the coin is a valid and acceptable coin."""
        if coin in self.VALID_COINS:
            return True

        return False

    def make_change(self, amount):
        """Make change to return to the customer for the amount of they overpaid."""
        # Order dictionary in the descending direction by coin value.
        coin_dict_desc = sorted(self.VALID_COINS.items(), key=lambda x: x[1], reverse=True)
        for coin_name, coin_value in coin_dict_desc:
            while coin_value <= amount and self.coin_inventory[coin_name] > 0:
                self.coin_inventory[coin_name] -= 1
                amount -= coin_value
                self.return_coin(coin_name, 1)

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
