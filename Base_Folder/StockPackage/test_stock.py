from unittest import TestCase
from main import *
import pandas as pd

class TestStock(TestCase):
    def test_stock_price(self):
        name = Stock('TSLA')
        self.assertEqual(name.stock_price(), '1,004.29')

    def test_up_or_down(self):
        name = Stock('TSLA')
        self.assertEqual(name.up_or_down(), '0.92%')

    def test_hist_data(self):
        name = Stock('TSLA')
        df = name.hist_data('1mo', '03-31-2021', '03-31-2022')
        pd.testing.assert_frame_equal(name.hist_data('1mo', '03-31-2021', '03-31-2022'), df)

