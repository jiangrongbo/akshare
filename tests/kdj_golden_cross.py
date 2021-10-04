import pandas as pd
import os
import talib as ta
import pysnowball as ball
import arrow
import akshare as ak

current_day = arrow.now().strftime('%Y%m%d')
stock_path = '/root/stock/stock_hist_data/'


def calc_kdj(symbol):
    stock_df = pd.read_csv(stock_path + symbol + '.csv')

    low_list = stock_df['最低'].rolling(9, min_periods=9).min()
    low_list.fillna(value=stock_df['最低'].expanding().min(), inplace=True)
    high_list = stock_df['最高'].rolling(9, min_periods=9).max()
    high_list.fillna(value=stock_df['最高'].expanding().max(), inplace=True)
    rsv = (stock_df['收盘'] - low_list) / (high_list - low_list) * 100

    stock_df['K'] = pd.DataFrame(rsv).ewm(com=2).mean()
    stock_df['D'] = stock_df['K'].ewm(com=2).mean()
    stock_df['J'] = 3 * stock_df['K'] - 2 * stock_df['D']

    stock_df['KDJ_INDICATOR'] = ''
    kdj_position = stock_df['K'] > stock_df['D']
    # 金叉
    stock_df.loc[kdj_position[(kdj_position == True) & (kdj_position.shift() == False)].index, 'KDJ_INDICATOR'] = '1'
    # 死叉
    stock_df.loc[kdj_position[(kdj_position == False) & (kdj_position.shift() == True)].index, 'KDJ_INDICATOR'] = '0'

    if stock_df.iloc[-1]['KDJ_INDICATOR'] == '1':
        print(symbol)
        if symbol[0] == '6':
            symbol = 'SH' + symbol
        else:
            symbol = 'SZ' + symbol
        ball.add_stock_to_item(current_day + 'KDJ', symbol)
    pass


def select_stock():
    if not ak.is_today_trade_day():
        return
    files = os.listdir(stock_path)

    for file_name in files:
        if '.csv' in file_name:
            symbol = file_name.replace(".csv", "")
            try:
                calc_kdj(symbol)
            except Exception as e:
                print("error", e)


def create_free():
    if not ak.is_today_trade_day():
        return
    ball.create_free_item(current_day + "KDJ")
    pass


if __name__ == "__main__":
    create_free()
    select_stock()
