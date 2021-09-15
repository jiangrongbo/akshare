import os

import arrow
import pandas as pd

import akshare as ak

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

stock_path = '/root/stock/stock_hist_data/'


def calc_hist_data():
    if not ak.is_today_trade_day():
        return
    stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
    stock_zh_a_spot_em_df = stock_zh_a_spot_em_df[
        ['代码', '今开', '最新价', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅', '涨跌额', '换手率']]
    stock_zh_a_spot_em_df.rename(columns={'今开': '开盘', '最新价': '收盘'}, inplace=True)
    stock_zh_a_spot_em_df['日期'] = arrow.now().strftime('%Y-%m-%d')
    for index, row in stock_zh_a_spot_em_df.iterrows():
        try:
            symbol = row['代码']
            file_name = stock_path + symbol + '.csv'
            if not os.path.exists(file_name):
                continue
            df = pd.read_csv(stock_path + symbol + '.csv', index_col=0)
            row.drop(labels='代码', axis=0, inplace=True)
            df = df.append(row, ignore_index=True)
            df.to_csv(file_name)
        except ValueError as e:
            print('ValueError:', e)

if __name__ == "__main__":
    calc_hist_data()
