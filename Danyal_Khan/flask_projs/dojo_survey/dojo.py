from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
	
	return render_template("index.html")

@app.route('/result', methods=["POST"])
def result():
	name = request.form['name']
	dojo = request.form['dojos']
	message = request.form['message']
	lang = request.form['lang']
	return render_template("result.html", name=name, dojo=dojo, message=message, lang=lang)

app.run(debug=True)