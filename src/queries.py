import sqlite3
import pandas as pd 
from build_db import get_conn

def test():
    conn = get_conn()
    df = pd.read_sql(
        " SELECT * FROM prix_carburants", conn)
    conn.close()
    return df


test = test()
print(test)