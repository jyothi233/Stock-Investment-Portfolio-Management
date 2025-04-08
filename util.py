import random
import psycopg2
import logging
import pandas as pd


conn_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'pgdb',
    'host': 'localhost',
    'port': '5432'  # default is 5432
}
def connect():
    conn=None
    try:
        conn=psycopg2.connect(**conn_params)

    except Exception as e:
        print("error occured while connecting "+e)
    return conn
def readData(schema,table):
    conn=None
    try:
        conn=connect()
        df=pd.read_sql("select * from {0}.{1}".format(schema,table),conn)
        return df
    except Exception as e:
        logging.error('ERROR:',e)

    finally:
        if not conn:
            conn.close()

def insert_all_into_table(schema,table,df):
        """
        insert dataframe into table using cursor.executemany()
        """
        tuples = [tuple(x) for x in df.to_numpy()]
        logging.info(f'tuples:{tuples}')
        print(tuples)
        cols = ', '.join(df.columns)
        values_placeholder = ', '.join(['%s'] * len(df.columns))
        query = f"INSERT INTO {schema}.{table} ({cols}) VALUES ({values_placeholder})"

        print(query)
        logging.info(f'query:{query}')
        conn=None
        try:

            conn =connect()
            cursor = conn.cursor()
            cursor.executemany(query, tuples)
            rowcount = cursor.rowcount
            conn.commit()
            logging.info(f"Insert into {table} [{rowcount} number of rows]")
            return rowcount
        except Exception as error:
            logging.error(f"Error: {error}" )
        finally:
            if not conn:
                conn.close()
        return 0
def executeQuery(query,val):
    conn=None
    try:
        conn=connect()
        cursor=conn.cursor()
        logging.info(f"INFO:{query}")
        if val:
            cursor.execute(query,val)
        else:
            cursor.execute(query)
        conn.commit()
        logging.info(f"Insert into  [{cursor.rowcount} number of rows]")

    except Exception as error:
        logging.error(f"Error:{error}")
    finally:
        conn.close()

