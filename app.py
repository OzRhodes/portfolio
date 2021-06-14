from flask import Flask, render_template, url_for	
import sqlite3
import os.path
import websocket
from datetime import datetime

app = Flask(__name__)

test_str = 'test string'

posts = [
	{'title': 'Post1',
	'auth': 'Oz'},
	{'title': 'Post2',
	'auth': 'Oz'}
]

#@app.route('/')
@app.route('/index')
def index():
	title = "Oz Rhodes - Home"
	#return "<h1>test</h1>"
	return render_template('index.html', title = title)
	
@app.route('/')
@app.route('/finance-bot')
def finance_bot():
	title= "Oz Rhodes - Finance Bot"
	
	#labels=['mon','tue','wed','thu','fri']
	#data = [1,2,4,3,5]
	


	base_endpoint = 'wss://stream.binance.com:9443'
	extension = '/ws/btcusdt@kline_1m'
	url = base_endpoint + extension
	
		
	if os.path.isfile('trades.db') == False:
		
		conn = sqlite3.connect('trades.db')
		c=conn.cursor()
		c.execute("""CREATE TABLE trades (id int PRIMARY KEY, time int NOT NULL, price real NOT NULL)""")
		print ("Opened database successfully - table created")
	else:
		conn = sqlite3.connect('trades.db')
		c = conn.cursor()
		print ("Opened database successfully")
		
	
	def on_close(ws):
		print("Closing")
	
	def on_message(ws, message):
		json_mess = json.loads(message)
		#print(json_mess)
		candle = json_mess['k']
		if candle['x']:
			#print(candle)
			trade_time = int(candle['t'])
			print(trade_time)
			price = float(candle['c'])
			sql_str= "INSERT INTO trades VALUES ({},{},{})".format('null', trade_time,  price)
		
			c.execute(sql_str)
		
		
			c.execute("SELECT * FROM trades")
		#print(c.fetchall())
			labels=[]
			data=[]
		
			for row in c:
				time_only = row[1]//1000
				time_only = str(datetime.fromtimestamp(time_only)).split()[1]
				print(time_only)
				print(row[2])
				labels.append(time_only)
				data.append(row[2])
				
		conn.commit()




		ws = websocket.WebSocketApp(url,on_message = on_message, on_close = on_close)
		
		ws.run_forever()
	
	return render_template('financechart.html', title = title, labels = labels, data = data)
	

#@app.route('/')
@app.route('/blog')
def blog():
	title = "Oz Rhodes - Blog"
	return render_template('blog.html', posts = posts)
  #return "<h1>test</h1>"

@app.route('/')
@app.route("/landing")
def landing():
	
	title = "Landing"
	return render_template('landing.html', title = title)
	

if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)
