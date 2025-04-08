import pandas as pd
from util import readData,insert_all_into_table
def stockExchangesLoad():
    df=readData('stockportfoliomgm','stocks')[['stockid']]
    expanded_df = pd.DataFrame(columns=df.columns.tolist() + ['stockexchange'])
    for i,row in df.iterrows():
        n_r=row.copy()
        n_r['stockexchange']='NSE'
        expanded_df=expanded_df._append(n_r,ignore_index=True)
        n_r = row.copy()
        n_r['stockexchange'] = 'BSE'
        expanded_df = expanded_df._append(n_r, ignore_index=True)
    insert_all_into_table('stockportfoliomgm','stockexchanges',expanded_df)


