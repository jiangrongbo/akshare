import unittest
import akshare as ak
import pandas as pd
import talib as ta

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class StockTest(unittest.TestCase):

    def test_stock_history(self):
        stock_zh_a_hist_df = ak.stock_zh_a_hist("688707")
        print(stock_zh_a_hist_df)

        dif, dea, hist = ta.MACD(stock_zh_a_hist_df['收盘'].astype(float).values, fastperiod=12, slowperiod=26,
                                 signalperiod=9)

        stock_zh_a_hist_df['date'] = stock_zh_a_hist_df['日期']

        macd_df = pd.DataFrame({'dif': dif[10:], 'dea': dea[10:], 'hist': hist[10:]},
                               index=stock_zh_a_hist_df['date'][10:], columns=['dif', 'dea', 'hist'])

        macd_df = macd_df.tail(2)

        if (macd_df.iloc[0, 0] <= macd_df.iloc[0, 1]) & (macd_df.iloc[1, 0] >= macd_df.iloc[1, 1]):
            print("true")

        pass
        print(macd_df)
        pass


if __name__ == '__main__':
    unittest.main()
