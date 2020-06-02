from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')


@app.route('/')
def homePage():
    return render_template("index.html")

@app.route('/portfolios/')
def portfolios():
    return render_template("Portfolios.html")

### START: THE VARIOUS PORTFOLIO PAGES ###

@app.route('/roberto/')
def robertoPortfolio():
    return render_template("robertoPortfolio.html")

### END: THE VARIOUS PORTFOLIO PAGES ###

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contactus/')
def contactUs():
    return render_template('contactus.html')

@app.route('/test/')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    # for when it needs to be deployed on AWS webservice
    # app.run(host='0.0.0.0', port='80')
    app.run()
