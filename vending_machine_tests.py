"""
    Tests for vending_machine.
    Author: John Wheeler
    Date: 08/29/2017
"""

import unittest
import vending_machine
from vending_machine import VendingMachine

class VendingMachineTest(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine()

    def test_is_valid_coin_with_nickel_should_return_true(self):
        self.assertTrue(self.machine.is_valid_coin(vending_machine.NICKEL))

    def test_is_valid_coin_with_dime_should_return_true(self):
        self.assertTrue(self.machine.is_valid_coin(vending_machine.DIME))

    def test_is_valid_coin_with_quarter_should_return_true(self):
        self.assertTrue(self.machine.is_valid_coin(vending_machine.QUARTER))

    def test_is_valid_coin_with_penny_should_return_false(self):
        self.assertFalse(self.machine.is_valid_coin(vending_machine.PENNY))

if __name__ == '__main__':
    unittest.main()
