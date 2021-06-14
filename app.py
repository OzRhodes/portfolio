from flask import Flask, render_template, url_for	
import sqlite3
import os.path
import websockets
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
def test():
	
	return render_template('test.html')
	#return "<h1>test</h1>"
	

@app.route('/')
#@app.route("/landing")
def landing():
	
	title = "Landing"
	return render_template('landing.html', title = title)
	

if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)
