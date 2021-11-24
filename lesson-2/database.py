# Import this to create database
import sqlite3
# creating a database
conn = sqlite3.connect('password.sqlite')
cur = conn.cursor()
try:
    # Creates a table woth columns
    cur.execute('CREATE TABLE password ( username VARCHAR, password VARCHAR, website VARCHAR)')
except:
    print('An error occured while trying to create table')

conn.commit()
conn.close()