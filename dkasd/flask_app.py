from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def info():
    return render_template('template1.html')


@app.route("/wait")
def wait():
    return render_template('template2.html')


@app.route("/comp1")
def comp1():
    return render_template('templatecomp1.html')


@app.route("/comp2")
def comp2():
    return render_template('templatecomp2.html')


@app.route("/comp3")
def comp3():
    return render_template('templatecomp3.html')


@app.route("/final")
def final():
    return render_template('template3.html')


@app.route("/card")
def card():
    return render_template('template4.html')


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
