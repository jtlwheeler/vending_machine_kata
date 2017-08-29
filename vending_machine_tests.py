import unittest
from vending_machine import VendingMachine

class VendingMachineTest(unittest.TestCase):
    def test_is_valid_coin_with_nickel_should_return_true(self):
        machine = VendingMachine()
        self.assertTrue(machine.is_valid_coin("NICKEL"))
    
    def test_is_valid_coin_with_dime_should_return_true(self):
        machine = VendingMachine()
        self.assertTrue(machine.is_valid_coin("DIME"))
