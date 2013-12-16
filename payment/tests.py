import unittest
from payment.methods import make_payment


class SimpleTest(unittest.TestCase):

    def test_make_payment_works1(self):
        # Issue a GET request.
        response = make_payment("Bla");

        # Check that the response is 200 OK.
        self.assertEqual("Made Payment! Bla", response)