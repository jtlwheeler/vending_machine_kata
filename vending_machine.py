"""
    Vending machine kata.
    Author: John Wheeler
    Date: 08/29/2017
"""

PENNY = "PENNY"
NICKEL = "NICKEL"
DIME = "DIME"
QUARTER = "QUARTER"

class VendingMachine():
    """Represents a vending machine."""

    # Coins that the vending machine are able to accept and their value.
    VALID_COINS = {NICKEL : 0.05, DIME : 0.10, QUARTER : 0.25}

    def __init__(self):
        # Monetary amount inserted by the customer.
        self.current_amount = 0.0

        # Acceptable coins and the number entered by the customer.
        self.inserted_coins = {NICKEL : 0, DIME : 0, QUARTER : 0}

    def insert_coin(self, coin):
        if self.is_valid_coin(coin):
            self.current_amount += self.VALID_COINS[coin]
            self.inserted_coins[coin] += 1

    def is_valid_coin(self, coin):
        """Returns True if the coin is a valid and acceptable coin."""
        if coin in self.VALID_COINS:
            return True

        return False
