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

    #VALID_COINS = [NICKEL, DIME, QUARTER]
    VALID_COINS = {NICKEL : 0.05, DIME : 0.10, QUARTER : 0.25}

    def is_valid_coin(self, coin):
        """Returns True if the coin is a valid and acceptable coin."""
        if coin in self.VALID_COINS:
            return True

        return False
