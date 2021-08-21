import unittest
import akshare as ak
import pandas as pd
import time

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 5000)


class StockTest(unittest.TestCase):
    # turnoverratio 换手率
    def test_stock_industry(self):
        stock_industry_df = pd.read_csv('stock_industry2021_08_20.csv')
        print(stock_industry_df.columns)
        stock_industry_df = stock_industry_df[[
            'code', 'name', 'trade', 'open', 'high', 'low', 'volume', 'amount', 'turnoverratio', 'per', 'pb',
            'industry']]

        stock_industry_df = stock_industry_df.query('per > 0')

        stock_industry_df["per"] = pd.to_numeric(stock_industry_df["per"], errors='coerce').fillna(0)
        stock_industry_df["pb"] = pd.to_numeric(stock_industry_df["pb"], errors='coerce').fillna(0)
        stock_industry_df["volume"] = pd.to_numeric(stock_industry_df["volume"], errors='coerce').fillna(0)
        stock_industry_df["amount"] = pd.to_numeric(stock_industry_df["amount"], errors='coerce').fillna(0)

        stock_industry_df = stock_industry_df.groupby(by=['industry'], group_keys=True).apply(
            lambda x: x.sort_values('per', ascending=False))
        stock_industry_df.to_csv('result.csv')
        print(stock_industry_df[['name','trade', 'per', 'industry']])

    def test_stock_info_sz_name_code(self):
        stock_info_sz_name_code_df = ak.stock_info_sz_name_code(indicator='A股列表')
        print(stock_info_sz_name_code_df)

    def test_stock_company_summary_info(self):
        stock_company_summary_info_df = ak.stock_company_summary_info()
        stock_company_summary_info_df.to_csv("stock_company_summary_info2021_08_24.csv")


if __name__ == '__main__':
    unittest.main()
