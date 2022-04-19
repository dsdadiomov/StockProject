import unittest
from Stock import *

class test(unittest.TestCase):
    name = Stock('TSLA')
    def check_price(self):
        price = name.stock_price()
        self.assertEqual(price,1004.29) # add assertion here


if __name__ == '__main__':
    unittest.main()
