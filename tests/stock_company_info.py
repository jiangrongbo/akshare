import akshare as ak

stock_company_summary_info_df = ak.stock_company_summary_info(169)
stock_company_summary_info_df.to_csv("stock_company_summary_info2021_08_22.csv")