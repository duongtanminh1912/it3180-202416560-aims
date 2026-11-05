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
