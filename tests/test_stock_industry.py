import unittest
import akshare as ak
import pandas as pd
import time

pd.set_option('display.max_rows', 5000)
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
        stock_industry_df.to_csv('stock_industry_result.csv')
        print(stock_industry_df[['code', 'name', 'trade', 'per', 'industry']])

    def test_stock_info_sz_name_code(self):
        stock_info_sz_name_code_df = ak.stock_info_sz_name_code(indicator='A股列表')
        print(stock_info_sz_name_code_df)

    def test_stock_company_summary_info(self):
        stock_company_summary_info_df = ak.stock_company_summary_info()
        stock_company_summary_info_df.to_csv("stock_company_summary_info2021_08_24.csv")

    def test_stock_company_summary_info_merge(self):
        pd1 = pd.read_csv('stock_company_summary_info2021_08_22.csv')

        pd2 = pd.read_csv('stock_company_summary_info2021_08_22_2.csv')
        pd1 = pd1.append(pd2, ignore_index=True)
        pd1['股票代码'] = pd1['股票代码'].apply(lambda x: str(x).rjust(6, '0'))
        pd1.drop('Unnamed: 0', axis=1, inplace=True)
        print(pd1)

        pd1.to_csv('stock_company_summary_info.csv')

    def test_merge(self):
        stock_industry_df = pd.read_csv('stock_industry2021_08_20.csv')
        stock_industry_df.drop_duplicates(inplace=True)
        stock_industry_df.drop('Unnamed: 0', axis=True, inplace=True)
        stock_industry_df['code'] = stock_industry_df['code'].apply(lambda x: str(x).rjust(6, '0'))

        print(stock_industry_df)
        stock_industry_df.to_csv('stock_industry.csv')

    def test_big_table(self):
        df1 = pd.read_csv('stock_industry.csv')
        # df2 = pd.read_csv('stock_company_summary_info.csv')
        # df3 = pd.merge(df1,df2,how='left', left_on=['code'],right_on=['股票代码'])
        print(df1['code'].apply(lambda x: str(x).rjust(6, '0')))

        # print(df1['股票名称'])
        # df3.to_csv('test.csv')
    # print(df1)
    # print(df3)


if __name__ == '__main__':
    unittest.main()
