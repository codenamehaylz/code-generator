from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = '0e1226ee99bc01c03ef7854b56215ba535246ffc00af41c2'

word = ["Word"]

@app.route("/")
def hello():
    return render_template('index.html', word=word)

@app.route("/generate/", methods=("GET", "POST"))
def generate_codes():
    if request.method == "POST":
        entered_word = request.form['word']
        if not entered_word:
            flash("You must enter a word or phrase!")
        else:
            word.clear()
            word.append(entered_word)
            return redirect(url_for('hello'))
        
    return render_template('generate.html')


if __name__ == '__main__':
     app.run(debug=True)