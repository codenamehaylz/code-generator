from flask import Flask, render_template, request, url_for, flash, redirect
from generate_function import generate_codes

app = Flask(__name__)
app.config["SECRET_KEY"] = '0e1226ee99bc01c03ef7854b56215ba535246ffc00af41c2'


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
        word = request.form.get('word')
        length = int(request.form.get('characters'))
        option = request.form.get('first_char')

        if not word:
            flash("You must enter a word or phrase!")
        else:
            user_input.clear()
            user_input.append({'word': word, 'length': length, 'first_letter_option': option})
            codes = generate_codes(word, length, option)
            generated_codes.clear()
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