#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('mime.db')
print ("Opened database successfully");

conn.execute('''CREATE TABLE Sign
         (ID text PRIMARY KEY     NOT NULL,
         LINK           TEXT    NOT NULL);''')
print ("Table created successfully");

conn.close()

