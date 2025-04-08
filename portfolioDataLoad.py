from faker import Faker
from util import readData,executeQuery
import random
from datetime import datetime,timedelta


def portfolioDataLoad():
    df=readData('stockportfoliomgm','users')

    fake=Faker()
    # Generate and insert 100 portfolio records
    for _ in range(1000):
        userId = random.uniform(1,100)
        description = fake.text(max_nb_chars=100)
        portfolioName = fake.word().capitalize() + ' Portfolio'
        portfolioCreatedAt = fake.date_this_month(before_today=True,after_today=False)
        portfolioUpdatedAt = fake.date_between_dates(datetime.now().date()-timedelta(days=6),datetime.now())
        currentBalance = round(random.uniform(1000, 10000000), 2)
        profit = round(random.uniform(0, 50000), 2)
        loss = round(random.uniform(0, 50000), 2)

        insert_query = """
        INSERT INTO stockPortfolioMGM.portfolio (
            userId, description, portfolioName, portfolioCreatedAt, 
            portfolioUpdatedAt, currentBalance, profit, loss
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        executeQuery(insert_query, (
            userId, description, portfolioName, portfolioCreatedAt,
            portfolioUpdatedAt, currentBalance, profit, loss
        ))


