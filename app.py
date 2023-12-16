from flask import (
    Flask,
    render_template,
    url_for,
    jsonify,
    request,
    redirect
)
from pymongo import MongoClient
import jwt
import datetime
from datetime import datetime 
import hashlib
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = './static/profile_pics'

SECRET_KEY = 'TRAVELUKI'
# hanya untuk latihan, dan sebaik nya dibuat lebih susah untuk projek

MONGODB_CONNECTION_STRING = 'mongodb://test:sparta@ac-ljccvx2-shard-00-00.sxulqfe.mongodb.net:27017,ac-ljccvx2-shard-00-01.sxulqfe.mongodb.net:27017,ac-ljccvx2-shard-00-02.sxulqfe.mongodb.net:27017/?ssl=true&replicaSet=atlas-uougez-shard-0&authSource=admin&retryWrites=true&w=majority'

client = MongoClient(MONGODB_CONNECTION_STRING)

db = client.dbtraveluki

TOKEN_KEY = 'mytoken'



app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('home.html')

@app.route('/sign_up/save')
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # id
        "password": password_hash,                                  # password
        "profile_name": username_receive,                           # user's name is set to their id by default
        "profile_pic": "",                                          # profile image file name
        "profile_pic_real": "profile_pics/profile_placeholder.png", # a default profile image
        "profile_info": ""                                          # a profile description
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})
    

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/discover')
def discover():
    token_receive = request.cookies.get("mytoken")
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.users.find_one({"username": payload["id"]})
        return render_template('discover.html', user_info=user_info)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="Your token has expired"))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="There was problem logging you in"))

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/discoveradm')
def discover_admin():
    return render_template('discoveradm.html')

@app.route('/edit-detail')
def edit_detail():
    return render_template('edit_detail.html')

@app.route('/editTGD')
def edit_tgd():
    return render_template('editTGD.html')

@app.route('/addTGD')
def add_tgd():
    return render_template('addTGD.html')

@app.route('/adddestination')
def add_destionation():
    return render_template('adddestination.html')



if __name__== '__main__':
    app.run('0.0.0.0',port=5000, debug=True)