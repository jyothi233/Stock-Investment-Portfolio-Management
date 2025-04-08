from util import executeQuery
from faker import Faker
import random
def userLoad():
    fake=Faker()
    for _ in range(100):
        name = fake.name()
        age = random.randint(18, 80)
        username = fake.user_name()
        userpassword = fake.password(length=12)
        address = fake.address()
        userdemataccno = fake.bban()
        useremailaddress = fake.email()
        usermobilenumber = fake.random_number(digits=10, fix_len=True)
        userpan = fake.bban()
        totalavailablefunds = round(random.uniform(1000, 1000000), 2)

        insert_query = """
        INSERT INTO stockportfoliomgm.users (
            "name", age, username, userpassword, address, userdemataccno, useremailaddress, 
            usermobilenumber, userpan, totalavailablefunds
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        executeQuery(insert_query,(
            name, age, username, userpassword, address, userdemataccno, useremailaddress,
            usermobilenumber, userpan, totalavailablefunds
        ))