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

    def test_insert_coin_with_nickel_and_check_inserted_amount_and_inserted_coins(self):
        self.machine.insert_coin(vm.NICKEL)
        self.assertEqual(0.05, self.machine.current_amount)
        self.assertEqual(1, self.machine.inserted_coins[vm.NICKEL])

    def test_insert_coin_with_different_coins_and_check_inserted_amount_and_inserted_coins(self):
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.NICKEL)
 
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.assertEqual(0.80, self.machine.current_amount)

        self.assertEqual(2, self.machine.inserted_coins[vm.NICKEL])
        self.assertEqual(2, self.machine.inserted_coins[vm.DIME])
        self.assertEqual(2, self.machine.inserted_coins[vm.QUARTER])

    def test_insert_coin_with_penny_should_be_place_in_coin_return(self):
        self.machine.insert_coin(vm.PENNY)
        self.assertIn(vm.PENNY, self.machine.coin_return)

    def test_return_coins_with_multiple_coins_and_check_coin_return_and_inserted_coin_bin(self):
        self.machine.insert_coin(vm.PENNY)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.NICKEL)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.return_inserted_coins()

        self.assertEqual(1, self.machine.coin_return[vm.PENNY])
        self.assertEqual(2, self.machine.coin_return[vm.NICKEL])
        self.assertEqual(1, self.machine.coin_return[vm.DIME])
        self.assertEqual(1, self.machine.coin_return[vm.QUARTER])
        
        self.assertEqual(0, self.machine.inserted_coins[vm.NICKEL])
        self.assertEqual(0, self.machine.inserted_coins[vm.DIME])
        self.assertEqual(0, self.machine.inserted_coins[vm.QUARTER])

if __name__ == '__main__':
    unittest.main()
