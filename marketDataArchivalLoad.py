import random

import pandas as pd
from util import readData,insert_all_into_table
from datetime import datetime,timedelta;
def loadMarketDataArchival():
    df=readData('stockportfoliomgm','stockexchanges')[['exchangeid','stockid']]
    print(df)

    today = datetime.now().date()

    dates_list = []
    for i in range(15):
        date=today - timedelta(days=i)
        if date.weekday() not in (5,6):
            dates_list.append(date)
    extended_df=pd.DataFrame(columns=df.columns.to_list()+['openingprice',
           'closingprice', 'dayhighestprice', 'daylowestprice', 'averagevolume',
           'averagebuyingvolume', 'averagesellingvolume', 'date'])
    for i,r in df.iterrows():
        for date in dates_list:
            temp_row=r.copy()
            temp_row['openingprice']=round(random.uniform(100,4000),2)
            temp_row['closingprice']=round(random.uniform(temp_row['openingprice']-(temp_row['openingprice']*random.randint(1,50))/100,temp_row['openingprice']+
                                    (temp_row['openingprice']*random.randint(1,50))/100),2)
            temp_row['dayhighestprice']=round(random.uniform(max(temp_row['openingprice'],temp_row['closingprice']),4000),2)
            temp_row['daylowestprice']=round(random.uniform(1000,min(temp_row['openingprice'],temp_row['closingprice'])),2)
            temp_row['averagevolume']=round(random.uniform(50000000,1000000000),2)
            temp_row['averagebuyingvolume']=round(random.uniform(50000000,1000000000),2)
            temp_row['averagesellingvolume'] = round(random.uniform(50000000, 1000000000), 2)
            temp_row['date']=date
            extended_df=extended_df._append(temp_row,ignore_index=True)

    insert_all_into_table('stockportfoliomgm','marketdataarchival',extended_df)



