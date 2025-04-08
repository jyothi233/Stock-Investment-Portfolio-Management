import logging

import pandas as pd
from util import readData,insert_all_into_table

def stockload():
    df=pd.read_csv('Data\\stock_metadata.csv')
    df_sector=readData('stockportfoliomgm','sector')
    print(df.columns)
    result = pd.merge(df, df_sector, left_on='Industry', right_on='sectorname', how='inner')[['sectorid','Company Name','Symbol']]

    result.rename(columns={'Company Name':'companyname'},inplace=True)
    print(result.columns)
    insert_all_into_table('stockportfoliomgm','stocks',result)



