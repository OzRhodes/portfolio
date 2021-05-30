from flask import Flask, render_template, url_for	

app = Flask(__name__)

test_str = 'test string'

posts = [
	{'title': 'Post1',
	'auth': 'Oz'},
	{'title': 'Post2',
	'auth': 'Andy'}
]

#@app.route('/')
@app.route('/index')
def index():
	title = "Oz Rhodes - Home"
	#return "<h1>test</h1>"
	return render_template('index.html', title = title)

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
