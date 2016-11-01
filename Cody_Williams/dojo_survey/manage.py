from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	languages = [
		"JavaScript",
		"PHP",
		"Ruby",
		"Python",
		"C#",
	]
	locations = [
		"Dallas",
		"San Jose",
		"Burbank",
		"Chicago",
		"Seattle",
	]
	return render_template('index.html', languages=languages, locations=locations)

@app.route('/surveys', methods=['POST'])
def create():
	name = request.form['asldkfj']
	location = request.form['location']
	language = request.form['language']
	comment = request.form['comment']
	return render_template('results.html', name=name, location=location, language=language, comment=comment)

app.run(debug=True)