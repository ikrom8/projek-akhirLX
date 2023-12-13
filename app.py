from flask import (
    Flask,
    render_template,
    url_for
)


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/discoveradm')
def discover_admin():
    return render_template('discoveradm.html')


if __name__== '__main__':
    app.run('0.0.0.0',port=5000, debug=True)