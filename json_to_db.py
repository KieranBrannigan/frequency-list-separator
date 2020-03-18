import sqlite3
import json


database_location = 'frequency_with_tokens_database.db'

with open('frequency_with_tokens.json','r',encoding='utf-8') as ReadFile:
    content = json.loads(ReadFile.read())

conn = sqlite3.connect(database_location)
cur = conn.cursor()

try:
    cur.execute("CREATE TABLE frequency (word, token)")
except sqlite3.OperationalError as e:
    #table already exists
    pass


for word,flag in content:
    t = (word,flag)
    cur.execute("INSERT INTO frequency VALUES (?,?)",t)

conn.commit()
conn.close()
