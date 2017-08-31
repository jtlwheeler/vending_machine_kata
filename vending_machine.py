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
        # Current coin inventory.
        # Key = coin name. Value = quantity.
        self.coin_inventory = {}

        # Coin return with number of coins.
        # Key = coin name. Value = quantity.
        self.coin_return = {}

        # Monetary amount inserted by the customer.
        self.current_amount = 0.0

        # Vending machine display unit.
        self._display = ""

        # Product dispense bin with the name of the product dispensed.
        self.product_dispense_bin = ""

        # Current product inventory. Product name and quantity.
        self.product_inventory = {}

        # Acceptable coins and the number entered by the customer.
        # Key = coin name. Value = quantity.
        self.inserted_coins = {}

        # Initialize the dictionaries with the keys of the coins that
        # can be accepted by the vending machine.
        for coin in self.VALID_COINS:
            self.coin_inventory[coin] = 0
            self.inserted_coins[coin] = 0

        for product in self.PRODUCTS:
            self.product_inventory[product] = 0

    @property
    def display(self):
        """Vending machine display."""
        if self._display:
            # Toggle the display to show the custom message so that the
            # standard display can be shown the next time it is checked.
            tmp_str = self._display
            self._display = ""
            return tmp_str

        if self.is_machine_sold_out():
            return "SOLD OUT"

        if self.current_amount > 0.0:
            return "$%.2f" % self.current_amount

        if self.exact_change_only():
            return "EXACT CHANGE ONLY"

        return "INSERT COIN"

    @display.setter
    def display(self, value):
        self._display = value

    def dispense_product(self, product):
        """
        Dispense the product once the user has entered enough money.
        Coins will be transferred into the coin inventory and the product
        moved into the product dispense bin for the customer to take.
        """
        if self.current_amount < self.PRODUCTS[product]:
            self.display = "PRICE $%.2f" % self.PRODUCTS[product]
            return

        # Move the inserted coins into the coin inventory.
        for coin in self.inserted_coins:
            if self.inserted_coins[coin] > 0:
                self.coin_inventory[coin] = self.inserted_coins[coin]
                self.inserted_coins[coin] = 0

        # Dispense the product.
        self.product_dispense_bin = product

        # Remove the product from the coin inventory.
        self.product_inventory[product] -= 1

        self.current_amount -= self.PRODUCTS[product]
        self._display = "THANK YOU"

    def exact_change_only(self):
        """Return True if exact change is needed."""
        min_coin = min(self.VALID_COINS.values())
        max_coin = max(self.VALID_COINS.values())

        coin_value_delta = round(max_coin - min_coin, 2)

        # In order to guarentee that change can be made, the coin inventory
        # must be able to make change for any amount up to the difference
        # in the minimum coin value and maximum value coin value beginning
        # at the minimum coin value and incrementing by the minimum coin
        # value afterwards.
        value_needed = min_coin
        while value_needed <= coin_value_delta:
            # See if change for this amount can be made.
            can_make_change = self.make_change(round(value_needed, 2), return_coin=False)
            if can_make_change is False:
                return True
            value_needed += min_coin

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
        """
        Make change to return to the customer for the amount of they overpaid.

        Algorithm:
            Start with the coin that has the largest value
            in the acceptable coins less than or equal to the amount needed.
            Remove the coin from the coin inventory if able to and subtract
            the coin's value from the amount needed. If the amount needed is
            now less than the current coin's value, continue on to the next
            coin.

        Args:
            amount (float): The amount of change needed.
            return_coin (bool): True if the coins should be placed in the coin return.
                                False if the coin inventory should not be modified.

        Returns:
            True if change can be made for the needed amount.
        """

        # "Order" dictionary in the descending direction by coin value.
        # i.e. {"QUARTER" : 0.25, "DIME" : 0.10, ...}
        # We still need the coin's key to remove it from the coin inventory
        # dictionary, so both the key and value is needed from the valid
        # coins dictionary.
        coin_dict_desc = sorted(self.VALID_COINS.items(), key=lambda x: x[1], reverse=True)
        for coin_name, coin_value in coin_dict_desc:
            while coin_value <= round(amount, 2) and self.coin_inventory[coin_name] > 0:
                amount -= coin_value
                if return_coin:
                    # Remove the coin from the coin inventory and return it
                    # to the customer.
                    self.coin_inventory[coin_name] -= 1
                    self.return_coin(coin_name, 1)

        return bool(round(amount, 2) == 0.0)

    def return_coin(self, coin, quantity):
        """Place the returned coin(s) in the return coin bin."""
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
