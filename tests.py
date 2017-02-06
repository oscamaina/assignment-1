import unittest
from prime import prime_num

class PrimeTestCase(unittest.TestCase):
    """Tests for prime.py"""

    def test_if_output_is_correct(self):
        """Test if output is correct"""
        self.assertEquals(prime_num(10),[2,3,5,7])

    def test_if_accepts_string(self):
        """Tests if the program aaccepts a string"""
        with self.assertRaises(TypeError):
            prime_num("String")

    def test_if_accepts_float(self):
        """Tests if the program accepts a float number"""
        with self.assertRaises(TypeError):
            prime_num("Float")

    def test_if_accepts_negative(self):
        """Tests if program accepts a negative number"""
        self.assertEquals(prime_num(-45), "Negative numbers are not accepted!!")

    def test_if_input_is_zero(self):
        """Tests if zero is a prime number"""
        self.assertEquals(prime_num(0), "Zero is not accepted!!")

    def test_if_input_is_one(self):
        """Tests if one is a prime number"""
        self.assertEquals(prime_num(1), "One is not a prime number")

    def test_if_includes_number_itself(self):
        """Tests when the final range number if prime is included in list"""
        self.assertIn(97, prime_num(97))

    def test_if_outputs_correctly_for_a_large_range(self):
        """Tests if outputs correct result for an incresead range"""
        self.assertEquals(len(prime_num(100)), 25)

    def test_if_accepts_lists(self):
        """Test if type list is accepted"""
        with self.assertRaises(TypeError):
            prime_num([])

    def test_if_accepts_dictionaries(self):
        """Test if dictionary is accepted"""
        with self.assertRaises(TypeError):
            prime_num({})
