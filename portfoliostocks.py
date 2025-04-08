from util import executeQuery,readData
import random
def loadPortfolioStocks():
    portfolios_ids=readData('stockportfoliomgm','portfolio')['portfolioid'].to_list()
    df=readData('stockportfoliomgm','stockexchanges')[['exchangeid','stockid']]
    stockExchangeIds=[[row[0],row[1]] for _,row in df.iterrows()]
    for _ in range(2000):
        portfolioid = random.choice(portfolios_ids)
        exchange= random.choice(stockExchangeIds)
        exchangeid=int(exchange[0])
        stockid=int(exchange[1])
        quantity = random.randint(1, 1000)
        averagebuyprice = round(random.uniform(10, 5000), 2)
        currentprice = round(random.uniform(10, 5000), 2)
        investedamount = round(quantity * averagebuyprice, 2)
        currentamount = round(quantity * currentprice, 2)
        profit = max(currentamount - investedamount, 0)
        loss = max(investedamount - currentamount, 0)
        profitpercentage = round((profit / investedamount) * 100 if investedamount != 0 else 0, 2)
        losspercentage = round((loss / investedamount) * 100 if investedamount != 0 else 0, 2)

        insert_query = """
        INSERT INTO stockportfoliomgm.portfoliostocks (
            portfolioid, exchangeid, stockid, quantity, averagebuyprice, currentprice,
            profit, loss, profitpercentage, losspercentage, investedamount, currentamount
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        executeQuery(insert_query, (
            portfolioid, exchangeid, stockid, quantity, averagebuyprice, currentprice,
            profit, loss, profitpercentage, losspercentage, investedamount, currentamount
        ))