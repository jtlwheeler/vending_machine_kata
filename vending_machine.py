class VendingMachine():
    def is_valid_coin(self, coin):
        if coin == "NICKEL" or coin == "DIME" or coin == "QUARTER":
            return True
