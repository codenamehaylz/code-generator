from flask import Flask, render_template, request, url_for, flash, redirect
from generate_function import generate_code

app = Flask(__name__)
app.config["SECRET_KEY"] = '0e1226ee99bc01c03ef7854b56215ba535246ffc00af41c2'

user_input = [{'word': 'Word',
               'length': 2,
               'first_letter_option': ''}]


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result/")
def result():
    return render_template('result.html', user_input = user_input)

@app.route("/generate/", methods=("GET", "POST"))
def generate_codes():
    if request.method == "POST":
        word = request.form.get('word')
        length = request.form.get('characters')
        option = request.form.get('first_char')


        if not word:
            flash("You must enter a word or phrase!")
        else:
            user_input.clear()
            user_input.append({'word': word, 'length': length, 'first_letter_option': option})
            return redirect(url_for('result'))
        
    return render_template('generate.html')


if __name__ == '__main__':
     app.run(debug=True)