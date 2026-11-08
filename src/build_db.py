import sqlite3
import pandas as pd #type: ignore
import os
import time
from urllib.request import urlretrieve

path = "data/prix-des-carburants-en-france.csv"

def get_conn():
    return sqlite3.connect("data/prix_carburants.db")

if (not os.path.exists(path) or (time.time() - os.path.getmtime(path) > 1800)):
    urlretrieve("https://www.data.gouv.fr/api/1/datasets/r/edd67f5b-46d0-4663-9de9-e5db1c880160", path)
    df = pd.read_csv(path, sep=";", compression="gzip")
    conn = get_conn()
    df.to_sql("prix_carburants", conn, if_exists="replace", index=False)
    conn.close()
