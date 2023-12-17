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


@app.route('/sign_up')
def sign_up():
    return render_template ('sign_up.html')
    

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/discover')
def discover():
    # token_receive = request.cookies.get("mytoken")
    # try:
    #     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    #     user_info = db.users.find_one({"username": payload["id"]})
    #     return render_template('discover.html', user_info=user_info)
    # except jwt.ExpiredSignatureError:
    #     return redirect(url_for("login", msg="Your token has expired"))
    # except jwt.exceptions.DecodeError:
    #     return redirect(url_for("login", msg="There was problem logging you in"))
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

@app.route('/edit-detail')
def edit_detail():
    return render_template('edit_detail.html')

@app.route('/editTGD')
def edit_tgd():
    return render_template('editTGD.html')

@app.route('/addTGD',)
def add_tgd():
    return render_template('addTGD.html')

# @app.route('/addTGD/save', methods=['POST'])
# def save_tgd():
#     name_receive = request.form.get('name_give')
#     age_receive = request.form.get('umur_give')
#     gender_receive = request.form.get('gender_give')
#     about_receive = request.form.get('about_give')
#     profile_receive = request.form.get('profile_give')
   
#     doc = {
#         "name": name_receive,                               # id
#         "profile_name": name_receive,                           # user's name is set to their id by default
#         "profile_pic": "",                                          # profile image file name
#         "profile_pic_real": "profile_pics/profile_placeholder.png", # a default profile image
#         "profile_info": ""                                          # a profile description
#     }
#     db.users.insert_one(doc)
#     return jsonify({'result': 'success'})

@app.route('/adddestination')
def add_destionation():
    return render_template('adddestination.html')

@app.route('/adddestinaai')
def add_destionasi():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'GET request complete!'})

@app.route('/detailadm')
def detail_adm():
    return render_template('detailadm.html')

@app.route('/cekpesanan')
def cek_pesanan():
    return render_template('cekpesanan.html')

@app.route('/cektiket')
def cek_tiket():
    return render_template('cek_tiket.html')

@app.route('/check_ticket', methods=['POST'])
def check_ticket():
    name = request.form['name']
    date = request.form['date']
    ticket_code = request.form['ticket_code']
    destination = request.form['destination']
    tourguide = request.form['tourguide']



if __name__== '__main__':
    app.run('0.0.0.0',port=5000, debug=True)