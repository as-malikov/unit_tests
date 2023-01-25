from unittest import TestCase

from store.calc import operations


class CalcTestCase(TestCase):
    def test_2plus3_5return(self):
        result = operations(2, 3, '+')
        self.assertEqual(5, result)

    def test_10minus3_7return(self):
        result = operations(10, 3, '-')
        self.assertEqual(7, result)

    def test_10multiply3_30return(self):
        result = operations(10, 3, '*')
        self.assertEqual(30, result)
