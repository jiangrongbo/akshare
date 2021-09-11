import unittest

import pandas as pd

import akshare as ak

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class StockTest(unittest.TestCase):

    def test_tool(self):
        print(ak.is_today_trade_day())


if __name__ == '__main__':
    unittest.main()
