#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('mime.db')
print ("Opened database successfully");
i=1
while(i):
    name=input("Enter image id\n")
    link=input("\nenter image name\n")
    

    conn.execute("INSERT INTO Sign (ID,LINK) \
          VALUES (?,?)",(name,link))

    
    print ("Records created successfully");
    conn.commit()

conn.close()
