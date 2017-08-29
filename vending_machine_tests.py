"""
    Tests for vending_machine.
    Author: John Wheeler
    Date: 08/29/2017
"""

import unittest
import vending_machine as vm
from vending_machine import VendingMachine

class VendingMachineTest(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine()

    def test_is_valid_coin_with_nickel_should_return_true(self):
        self.assertTrue(self.machine.is_valid_coin(vm.NICKEL))

    def test_is_valid_coin_with_dime_should_return_true(self):
        self.assertTrue(self.machine.is_valid_coin(vm.DIME))

    def test_is_valid_coin_with_quarter_should_return_true(self):
        self.assertTrue(self.machine.is_valid_coin(vm.QUARTER))

    def test_is_valid_coin_with_penny_should_return_false(self):
        self.assertFalse(self.machine.is_valid_coin(vm.PENNY))

    def test_coin_values(self):
        self.assertEqual(0.05, self.machine.VALID_COINS[vm.NICKEL])
        self.assertEqual(0.10, self.machine.VALID_COINS[vm.DIME])
        self.assertEqual(0.25, self.machine.VALID_COINS[vm.QUARTER])

if __name__ == '__main__':
    unittest.main()
