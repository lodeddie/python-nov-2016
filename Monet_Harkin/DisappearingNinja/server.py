from flask import Flask, render_template, redirect
app= Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/ninja")
def ninjas():
	return render_template("ninjas.html")

@app.route("/ninja/<color>")
def each_ninja(color):
	if color == "red":
		image = "raphael.jpg"
		title = "Raphael"
		alt = "Picture of Raphael"
	elif color == "blue":
		image = "leonardo.jpg"
		title = "Leonardo"
		alt = "Picture of Leonardo"
	elif color == "orange":
		image = "michelangelo.jpg"
		title = "Michelangelo"
		alt = "Picture of Michelangelo"
	elif color == "purple":
		image = "donatello.jpg"
		title = "Donatello"
		alt = "Picture of Donatello"
	else:
		image = "notapril.jpg"
		title = "Not a Turtle - April"
		alt= "Picture of Megan Fox (Not a ninja turtle)"

	return render_template("ninjaColor.html", image=image, title=title, alt=alt)

app.run(debug=True)