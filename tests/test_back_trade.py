import unittest

import backtrader as bt
import pandas as pd

import akshare as ak

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class StockTest(unittest.TestCase):

    def test_stock_back_trade(self):
        stock_zh_a_hist_df = ak.stock_zh_a_hist("000001")
        print(stock_zh_a_hist_df)

        columns = {
            '日期': 'date',
            '开盘': 'open',
            '收盘': 'close',
            '最高': 'high',
            '最低': 'low',
            '成交量': 'volume',
            '成交额': 'amount',
            '振幅': 'amplitude',
            '涨跌幅': 'applies',
            '涨跌额': 'applies_amount',
            '换手率': 'turnover_rate'
        }

        stock_zh_a_hist_df.rename(columns=columns, inplace=True)
        stock_zh_a_hist_df['date'] = pd.to_datetime(stock_zh_a_hist_df['date'])
        stock_zh_a_hist_df.set_index('date', inplace=True)
        print(stock_zh_a_hist_df)

        class MyCross(bt.Strategy):

            def start(self):
                pass

            def next(self):
                print('hello')

        cerebro = bt.Cerebro()
        cerebro.addstrategy(MyCross)

        data0 = bt.feeds.PandasData(dataname=stock_zh_a_hist_df)
        cerebro.adddata(data0)

        cerebro.run()
        cerebro.plot(style='candle')
        pass


if __name__ == '__main__':
    unittest.main()
