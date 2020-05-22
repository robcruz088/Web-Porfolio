from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def basics2(name=None):
    return render_template("basics2.html", name=name)

@app.route('/basics2a/')
def basics2a():
    return render_template("basics2a.html")

@app.route('/basics2b/')
def basics2b():
    return render_template("basics2b.html")

if __name__=='__main__':
    # for AWS deployment
    app.run(host= '0.0.0.0', port='80')