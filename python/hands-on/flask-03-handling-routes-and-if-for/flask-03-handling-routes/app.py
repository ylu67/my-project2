from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first = "This is my first condition experience."
    return render_template('index.html', message = first)

@app.route("/yalcin")
def mylist():
    names = ["Ahmet Arif", "Salih", "Tarkan", "Suat"]
    return render_template('body.html', object = names)

    return render_template('')












if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)