from util import executeQuery
def marketDataLoad():
    query=f"""insert into stockportfoliomgm.marketdata (exchangeid, 
            stockid, openingprice, closingprice, dayhighestprice, 
            daylowestprice, averagevolume, averagebuyingvolume, 
            averagesellingvolume) 
            select exchangeid, stockid, openingprice, closingprice, 
            dayhighestprice, daylowestprice, averagevolume, averagebuyingvolume, 
            averagesellingvolume from stockportfoliomgm.marketdataarchival m 
            where date=current_date;"""
    executeQuery(query,val=None)