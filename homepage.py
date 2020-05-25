from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def homepage(name=None):
    return render_template("homepage.html")

@app.route('/basics2a/')
def basics2a():
    return render_template("basics2a.html")

@app.route('/basics2b/')
def basics2b():
    return render_template("basics2b.html")

if __name__=='__main__':
    # for when it needs to be deployed on AWS webservice
    # app.run(host='0.0.0.0', port='80')
    app.run() 