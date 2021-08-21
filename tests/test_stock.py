# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Date: 2020/10/12 18:16
Desc: To test intention, just write test code here!
"""
import akshare as ak
import pandas as pd
import time

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def test_industry():
    stock_sector = ak.stock_sector_spot(indicator='行业')

    stock_sector["涨跌幅"] = pd.to_numeric(stock_sector["涨跌幅"], errors='coerce').fillna(0)

    stock_sector = stock_sector.sort_values(by='涨跌幅')
    print(stock_sector)
    sector_detail_df = pd.DataFrame()

    for index, row_data in stock_sector.iterrows():
        tmp_sector_detail = ak.stock_sector_detail(sector=row_data['label'])
        time.sleep(1)
        tmp_sector_detail['industry'] = row_data['板块']
        sector_detail_df = sector_detail_df.append(tmp_sector_detail, ignore_index=True)

    return sector_detail_df


def test_industry_local():
    pd.read_csv('stock_industry2021_08_20.csv')


if __name__ == "__main__":
    test_industry_local()
