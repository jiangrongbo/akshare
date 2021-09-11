import akshare as ak
import time
import pandas as pd
import os
import arrow

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
stock_zh_a_spot_em_df = stock_zh_a_spot_em_df[['代码', '今开', '最新价', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅', '涨跌额', '换手率']]
stock_zh_a_spot_em_df.rename(columns={'今开': '开盘', '最新价': '收盘'}, inplace=True)
stock_zh_a_spot_em_df['日期'] = arrow.now().strftime('%Y-%m-%d')
print(stock_zh_a_spot_em_df)
for index, row in stock_zh_a_spot_em_df.iterrows():
    try:
        symbol = row['代码']
        if symbol == '688103':
            if not os.path.exists(symbol + '.csv'):
                continue
            df = pd.read_csv(symbol + '.csv', index_col=0)
            row.drop(labels='代码', axis=0, inplace=True)
            df = df.append(row, ignore_index=True)
            print(df)

    except ValueError as e:
        print('ValueError:', e)
