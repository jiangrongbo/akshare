import akshare as ak
import time
import pandas as pd
import os

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
for index, row in stock_zh_a_spot_em_df.iterrows():
    symbol = row['代码']
    if os.path.exists(symbol + '.csv'):
        continue
    print(symbol)
    try:
        stock_zh_a_m2_hist_df = ak.stock_zh_a_m2_hist(symbol)
        stock_zh_a_m2_hist_df.to_csv(symbol + '.csv')
        time.sleep(2)
    except ValueError as e:
        print('ValueError:', e)
