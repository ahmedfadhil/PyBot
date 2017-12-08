import sqlite3
import json
from _datetime import datetime

timeframe = '2015-05'
sql_transaction = []
connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply
(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT,
unix INT, score INT)""")


if __name__ == "__manin__":
    create_table()

    row_counter = 0
    paired_row = 0
with open("add your link here".format(timeframe.split('-')[0], timeframe), buffer=1000) as f:
    pass
