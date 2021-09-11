import pandas as pd
import os
import talib as ta
import pysnowball as ball
import arrow

current_day = arrow.now().strftime('%Y%M%d')
stock_path = '/root/stock/stock_hist_data/'


def calc_macd(symbol):
    stock_df = pd.read_csv(stock_path + symbol + '.csv')

    dif, dea, hist = ta.MACD(stock_df['收盘'].astype(float).values, fastperiod=12, slowperiod=26,
                             signalperiod=9)

    stock_df['date'] = stock_df['日期']

    macd_df = pd.DataFrame({'dif': dif[10:], 'dea': dea[10:], 'hist': hist[10:]},
                           index=stock_df['date'][10:], columns=['dif', 'dea', 'hist'])

    macd_df = macd_df.tail(2)

    if (macd_df.iloc[0, 0] <= macd_df.iloc[0, 1]) & (macd_df.iloc[1, 0] >= macd_df.iloc[1, 1]):
        if symbol[0] == '6':
            symbol = 'SH' + symbol
        else:
            symbol = 'SZ' + symbol
        ball.add_stock_to_item(current_day, symbol)
        print(symbol)
    pass


def select_stock():
    files = os.listdir(stock_path)

    for file_name in files:
        if '.csv' in file_name:
            symbol = file_name.replace(".csv", "")
            try:
                calc_macd(symbol)
            except Exception as e:
                print("error", e)


def create_free():
    ball.create_free_item(current_day)
    pass


if __name__ == "__main__":
    create_free()
    select_stock()
