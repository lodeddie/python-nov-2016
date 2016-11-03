from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "mysecretkey"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_users():

    vName = request.form['name']
    vEmail = request.form['email']
    vLanguage = request.form['language']
    vLocation = request.form['location']
    vComment = request.form['comment']

    if (vName == '') or (vEmail == '') or (len(vComment)>120):
        if (vName == ''):
            flash("name cannot be empty!")

        if (vEmail == ''):
            flash("email cannot be empty!")

        if (len(vComment)> 120):
            flash("comment cannot be greather than 120 characters")
        return redirect('/')
    else:
        return render_template("survey_results.html", name=vName, email=vEmail, language=vLanguage, location=vLocation, comment=vComment)

@app.route('/GoBack', methods=['POST'])
def go_back():

    return redirect('/')



app.run(debug=True)
