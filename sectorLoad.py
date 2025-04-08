import pandas as pd
import random
from util import insert_all_into_table

def sectorLoad():
    sectors=list(set(['AUTOMOBILE','CONSUMER GOODS','FINANCIAL SERVICES','AUTOMOBILE','FINANCIAL SERVICES',
                 'FINANCIAL SERVICES','TELECOM','ENERGY','CONSUMER GOODS','PHARMA','METALS',
                 'PHARMA','AUTOMOBILE','ENERGY','CEMENT & CEMENT PRODUCTS','IT','FINANCIAL SERVICES',
                 'FINANCIAL SERVICES','AUTOMOBILE','METALS','CONSUMER GOODS','FINANCIAL SERVICES',
                 'FINANCIAL SERVICES','TELECOM','IT','ENERGY','CONSUMER GOODS','METALS',
                 'FINANCIAL SERVICES','CONSTRUCTION','AUTOMOBILE','AUTOMOBILE','CONSUMER GOODS',
                 'ENERGY','ENERGY','ENERGY','ENERGY','FINANCIAL SERVICES','CEMENT & CEMENT PRODUCTS','PHARMA','AUTOMOBILE','METALS','IT','IT','CONSUMER GOODS',
                 'CEMENT & CEMENT PRODUCTS','FERTILISERS & PESTICIDES','METALS','IT','MEDIA & ENTERTAINMENT']))
    df_sector=pd.DataFrame({
    'sectorName':sectors,
    'sectorMarketcap': [round(random.uniform(10000000,99999999),2) for _ in range(len(sectors))]
    })
    insert_all_into_table('stockportfoliomgm','sector',df_sector)