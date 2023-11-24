from flask import Flask, render_template, request, url_for, flash, redirect
from generate_function import generate_codes
import os
import uuid

app = Flask(__name__)
SECRET_KEY = os.environ.get('APP_SECRET_KEY', uuid.uuid4().hex)
app.config["SECRET_KEY"] = SECRET_KEY


# Store user input and generated codes to display on results page
user_input = [{'word': 'Word',
               'length': 2,
               'first_letter_option': ''}]

generated_codes = []


# -- ENDPOINTS --

# Index page showing input form
@app.route("/", methods=("GET", "POST"))
def generate():
    if request.method == "POST":
        word = request.form.get('word').replace(" ", "")
        length = int(request.form.get('characters'))
        option = request.form.get('first_char')

        if not word:
            flash("You must enter a word or phrase!")
            
        if len(word) < length:
            flash("Please enter a word that is longer than number of characters selected.")

        else:
            # Clear variables first
            user_input.clear()
            generated_codes.clear()
            # Store user's inputs and generated codes in our variables
            user_input.append({'word': word, 'length': length, 'first_letter_option': option})
            codes = generate_codes(word, length, option)
            for code in codes:
                generated_codes.append(code)
                
            return redirect(url_for('result'))
        
    return render_template('index.html')


# Results page to display generated codes
@app.route("/result/")
def result():
    return render_template('result.html', 
                           user_input=user_input,
                           generated_codes=generated_codes,
                           len=len(generated_codes))


if __name__ == '__main__':
     app.run(debug=True)