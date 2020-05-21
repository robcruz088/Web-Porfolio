from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    return render_template("basics2.html", name=name)

if __name__=='__main__':
    app.run()