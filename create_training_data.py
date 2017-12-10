import sqlite3
import json
import pandas as pd
from _datetime import datetime

timeframes = '2015-05'

for timeframe in timeframes:
    connection = sqlite3.connect('{}.db'.format(timeframe))
    c = connection.cursor()
    limit = 5000
    last_unix = 0
    cur_length = limit
    counter = 0
    test_done = False

    while cur_length == limit:
        df = pd.read_sql(
            "SELECT * FROM parent_reply WHERE unix > {} AND parent NOT NULL AND score >0 ORDER BY unix ASC LIMIT {}".format(
                last_unix, limit), connection)
        last_unix = df.tail(1)['unix'].values[0]
        cur_length = len(df)
        if not test_done:
            with open("test.from",'a', encoding='utf8') as f:
                
