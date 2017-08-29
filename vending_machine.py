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

    VALID_COINS = [NICKEL, DIME, QUARTER]

    def is_valid_coin(self, coin):
        """Returns True if the coin is a valid and acceptable coin."""
        if coin in self.VALID_COINS:
            return True

        return False
