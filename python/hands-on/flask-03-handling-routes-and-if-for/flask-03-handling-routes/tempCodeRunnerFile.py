from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    first = "This is my first conditition experience"
    return render_template('index.html', message = first)
    











if __name__ == '__main__':
    app.run(debug=True)