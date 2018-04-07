#!/usr/bin/python

import sqlite3
import tkinter
import sign
from PIL import Image, ImageTk

def select(text):
   conn = sqlite3.connect('mime.db')
   print ("Opened database successfully")

   '''import os.path

   BASE_DIR = os.path.dirname(os.path.abspath(__file__))
   db_path = os.path.join(BASE_DIR, "img.db")
   with sqlite3.connect(db_path) as conn:'''

   cursor = conn.execute("SELECT id, link from Sign")
   for row in cursor:
      if text==row[0]:   
         print (row[0])
         sign.attach(row[1])
   print ("Operation done successfully");
   conn.close()





