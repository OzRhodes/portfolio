import os
import sqlite3
import random



if os.path.isfile('trades.db') == False:
	
	conn = sqlite3.connect('trades.db')
	c=conn.cursor()
	c.execute("""CREATE TABLE trades (id int PRIMARY KEY, time int NOT NULL, price real NOT NULL)""")
	print ("Opened database successfully - table created")
else:
	conn = sqlite3.connect('trades.db')
	c = conn.cursor()
	print ("Opened database successfully")
	
trade_time = 1622726000
minute = 60000
price = 37950
for i in range (20):
	trade_time += minute
	price_change = random.randint(-5,5)
	price += price_change 
	
	sql_str= "INSERT INTO trades VALUES ({},{},{})".format('null', trade_time,  price)
	
	c.execute(sql_str)

c.execute("SELECT * FROM trades")
records = c.fetchall()
for row in records:
	print(row[1])
	print(row[2])
	
		
conn.commit()
	
