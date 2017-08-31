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

    def test_return_coin_with_nickel_and_check_current_amount(self):
        self.machine.insert_coin(vm.NICKEL)
        self.assertEqual(0.05, self.machine.current_amount)

        self.machine.return_inserted_coins()
        self.assertEqual(0.0, self.machine.current_amount)

    def test_check_cola_price(self):
        self.assertEqual(1.0, self.machine.PRODUCTS[vm.COLA])

    def test_check_chip_price(self):
        self.assertEqual(0.50, self.machine.PRODUCTS[vm.CHIPS])

    def test_check_candy_price(self):
        self.assertEqual(0.65, self.machine.PRODUCTS[vm.CANDY])

    def test_select_cola_without_enough_money(self):
        self.machine.select_cola()
        self.assertEqual("", self.machine.product_dispense_bin)

    def test_select_cola_wth_exact_money(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_cola()
        self.assertEqual(vm.COLA, self.machine.product_dispense_bin)

    def test_select_cola_with_exact_money_and_check_coin_inventory(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_cola()

        self.assertEqual(0.0, self.machine.current_amount)
        self.assertEqual(4, self.machine.coin_inventory[vm.QUARTER])
        self.assertEqual(vm.COLA, self.machine.product_dispense_bin)

    def test_select_cola_with_extra_money_and_check_coin_inventory(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.select_cola()

        self.assertEqual(0.05, round(self.machine.current_amount, 2))
        self.assertEqual(3, self.machine.coin_inventory[vm.QUARTER])
        self.assertEqual(3, self.machine.coin_inventory[vm.DIME])
        self.assertEqual(vm.COLA, self.machine.product_dispense_bin)

    def test_select_chips_without_enough_money(self):
        self.machine.select_chips()
        self.assertEqual("", self.machine.product_dispense_bin)

    def test_select_chips_with_exact_money_and_check_coin_inventory(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_chips()

        self.assertEqual(0.0, self.machine.current_amount)
        self.assertEqual(2, self.machine.coin_inventory[vm.QUARTER])
        self.assertEqual(vm.CHIPS, self.machine.product_dispense_bin)

    def test_select_chips_with_extra_money_and_check_coin_inventory(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.select_chips()

        self.assertEqual(0.05, round(self.machine.current_amount, 2))
        self.assertEqual(1, self.machine.coin_inventory[vm.QUARTER])
        self.assertEqual(3, self.machine.coin_inventory[vm.DIME])
        self.assertEqual(vm.CHIPS, self.machine.product_dispense_bin)

    def test_select_candy_without_enough_money(self):
        self.machine.select_candy()
        self.assertEqual("", self.machine.product_dispense_bin)

    def test_select_candy_with_exact_money_and_check_coin_inventory(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.NICKEL)

        self.machine.select_candy()

        self.assertEqual(0.0, self.machine.current_amount)
        self.assertEqual(2, self.machine.coin_inventory[vm.QUARTER])
        self.assertEqual(1, self.machine.coin_inventory[vm.DIME])
        self.assertEqual(1, self.machine.coin_inventory[vm.NICKEL])
        self.assertEqual(vm.CANDY, self.machine.product_dispense_bin)
    
    def test_select_candy_with_extra_money_and_check_coin_inventory(self):
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.DIME)

        self.machine.select_candy()

        self.assertEqual(0.05, round(self.machine.current_amount, 2))
        self.assertEqual(2, self.machine.coin_inventory[vm.QUARTER])
        self.assertEqual(2, self.machine.coin_inventory[vm.DIME])
        self.assertEqual(vm.CANDY, self.machine.product_dispense_bin)

    def test_make_change_for_five_cents_with_one_nickel_in_coin_inventory(self):
        self.machine.coin_inventory[vm.NICKEL] += 1
        self.machine.make_change(0.05)
        self.assertEqual(1, self.machine.coin_return[vm.NICKEL])

    def test_make_change_for_ten_cents_with_two_nickels(self):
        self.machine.coin_inventory[vm.NICKEL] += 2
        self.machine.make_change(0.10)
        self.assertEqual(2, self.machine.coin_return[vm.NICKEL])
        self.assertEqual(0, self.machine.coin_inventory[vm.NICKEL])

    def test_make_change_for_ten_cents_with_one_dime(self):
        self.machine.coin_inventory[vm.DIME] += 1
        self.machine.make_change(0.10)
        self.assertEqual(1, self.machine.coin_return[vm.DIME])
        self.assertEqual(0, self.machine.coin_inventory[vm.DIME])

    def test_make_change_for_fifteen_cents_with_three_nickels(self):
        self.machine.coin_inventory[vm.NICKEL] = 3
        self.machine.make_change(0.15)
        self.assertEqual(3, self.machine.coin_return[vm.NICKEL])
        self.assertEqual(0, self.machine.coin_inventory[vm.NICKEL])

    def test_make_change_for_fifteen_cents_with_one_nickel_and_one_dime(self):
        self.machine.coin_inventory[vm.NICKEL] = 1
        self.machine.coin_inventory[vm.DIME] = 1
        self.machine.make_change(0.15)
        self.assertEqual(1, self.machine.coin_return[vm.NICKEL])
        self.assertEqual(1, self.machine.coin_return[vm.DIME])
        self.assertEqual(0, self.machine.coin_inventory[vm.NICKEL])
        self.assertEqual(0, self.machine.coin_inventory[vm.DIME])

    def test_make_change_for_twenty_cents_with_four_nickels(self):
        self.machine.coin_inventory[vm.NICKEL] = 4
        self.machine.make_change(0.20)
        self.assertEqual(4, self.machine.coin_return[vm.NICKEL])
        self.assertEqual(0, self.machine.coin_inventory[vm.NICKEL])

    def test_make_change_for_twenty_cents_with_two_nickels_and_one_dimes(self):
        self.machine.coin_inventory[vm.NICKEL] = 2
        self.machine.coin_inventory[vm.DIME] = 1
        self.machine.make_change(0.20)
        self.assertEqual(2, self.machine.coin_return[vm.NICKEL])
        self.assertEqual(1, self.machine.coin_return[vm.DIME])
        self.assertEqual(0, self.machine.coin_inventory[vm.NICKEL])
        self.assertEqual(0, self.machine.coin_inventory[vm.DIME])

    def test_make_change_for_twenty_cents_with_two_dimes(self):
        self.machine.coin_inventory[vm.DIME] = 2
        self.machine.make_change(0.20)
        self.assertEqual(2, self.machine.coin_return[vm.DIME])
        self.assertEqual(0, self.machine.coin_inventory[vm.DIME])

    def test_is_machine_sold_out_should_return_true(self):
        self.assertTrue(self.machine.is_machine_sold_out())

    def test_is_machine_sold_out_with_cola_should_return_false(self):
        self.machine.product_inventory[vm.COLA] = 1
        self.assertFalse(self.machine.is_machine_sold_out())

    def test_is_machine_sold_out_with_chips_should_return_false(self):
        self.machine.product_inventory[vm.CHIPS] = 1
        self.assertFalse(self.machine.is_machine_sold_out())

    def test_is_machine_sold_out_with_candy_should_return_false(self):
        self.machine.product_inventory[vm.CANDY] = 1
        self.assertFalse(self.machine.is_machine_sold_out())

    def test_select_chips_and_remove_from_product_inventory(self):
        self.machine.product_inventory[vm.CHIPS] = 1
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_chips()

        self.assertEqual(0, self.machine.product_inventory[vm.CHIPS])

    def test_select_cola_and_remove_from_product_inventory(self):
        self.machine.product_inventory[vm.COLA] = 1
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)

        self.machine.select_cola()

        self.assertEqual(0, self.machine.product_inventory[vm.COLA])

    def test_select_candy_and_remove_from_product_inventory(self):
        self.machine.product_inventory[vm.CANDY] = 1
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.QUARTER)
        self.machine.insert_coin(vm.DIME)
        self.machine.insert_coin(vm.NICKEL)

        self.machine.select_candy()

        self.assertEqual(0, self.machine.product_inventory[vm.CANDY])

    def test_exact_change_only_should_return_true(self):
        self.assertTrue(self.machine.exact_change_only())

    def test_exact_change_only_should_return_false_with_coins(self):
        self.machine.coin_inventory[vm.NICKEL] = 3
        self.machine.coin_inventory[vm.DIME] = 3

        self.assertFalse(self.machine.exact_change_only())

if __name__ == '__main__':
    unittest.main()
