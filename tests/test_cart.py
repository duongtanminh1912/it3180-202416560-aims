import contextlib
import io
import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_limit_twenty(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            for i in range(20):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(i))))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc("21")))
        self.assertEqual(len(cart.items), 20)

    def test_total_and_remove(self):
        cart = Cart()
        dvd = DigitalVideoDisc("A", cost=19.95)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertTrue(cart.add_dvd(dvd))
            self.assertAlmostEqual(cart.total_cost(), 19.95)
            self.assertTrue(cart.remove_dvd(dvd))
            self.assertFalse(cart.remove_dvd(dvd))
        self.assertAlmostEqual(cart.total_cost(), 0)

    def test_print_empty(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            Cart().print_cart()
        self.assertEqual(output.getvalue(), "The cart is empty.\n")

    def test_discount_and_bounds(self):
        cart = Cart()
        cart.items = [DigitalVideoDisc("A", cost=100)]
        self.assertAlmostEqual(cart.total_cost_with_discount(20), 80)
        self.assertAlmostEqual(cart.total_cost_with_discount(0), 100)
        self.assertAlmostEqual(cart.total_cost_with_discount(100), 0)
        for percent in (-1, 101):
            with self.assertRaises(ValueError):
                cart.total_cost_with_discount(percent)

    def test_sort_by_title_in_place(self):
        cart = Cart()
        a, b = DigitalVideoDisc("A", cost=20), DigitalVideoDisc("B", cost=10)
        cart.items = [b, a]
        items = cart.items
        cart.sort_by_title()
        self.assertIs(cart.items, items)
        self.assertEqual(cart.items, [a, b])

    def test_sort_by_cost_in_place_and_stable(self):
        cart = Cart()
        a, b, c = (DigitalVideoDisc("A", cost=20), DigitalVideoDisc("B", cost=10), DigitalVideoDisc("C", cost=10))
        cart.items = [a, b, c]
        items = cart.items
        cart.sort_by_cost()
        self.assertIs(cart.items, items)
        self.assertEqual(cart.items, [b, c, a])
        empty = Cart()
        empty.sort_by_title()
        empty.sort_by_cost()
        self.assertEqual(empty.items, [])
