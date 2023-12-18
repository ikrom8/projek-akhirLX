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
from flask_cors import CORS

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['UPLOAD_FOLDER'] = './static/default-image.jpg'

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

@app.route('/get_data')
def get_data():
    articles = list(db.destination.find({},{'_id' : False}))
    return jsonify({'articles':articles})

@app.route('/edit-detail')
def edit_detail():
    return render_template('edit_detail.html')

@app.route('/editTGD')
def edit_tgd():
    return render_template('editTGD.html')

@app.route('/addTGD', methods=["GET"])
def show_tgd():
    return render_template('addTGD.html')

@app.route('/addTourGD', methods=["POST"])
def add_tour_guide():
    id_give = request.form.get('id_give')
    name_give = request.form.get('name_give')
    age_give = request.form.get('umur_give')
    gender_give = request.form.get('gender_give')
    about_give = request.form.get('about_give')
    profile_give = request.form.get('profile_give')

    # Simpan data tour guide ke dalam list
    tour_guide = {
        'id': id_give,
        'name': name_give,
        'age': age_give,
        'gender': gender_give,
        'about': about_give,
        'profile': profile_give
    }
    db.tourguide.insert_one(tour_guide)

    return jsonify({'status': 'success'})


@app.route('/adddestination')
def add_destionation():
    return render_template('adddestination.html')

# @app.route('/adddestinasi',methods=['GET'])
# def show_destinasi():
#     # sample_receive= request.args.get('sample_give')
#     # print(sample_receive)
#     articles = list(db.destination.find({},{'_id' : False}))
#     return jsonify({'articles':articles})

@app.route('/adddestinasi', methods=['POST'])
def add_destinasi():
        
        id_receive = request.form["id_give"]
        image_receive = request.form["image_give"]
        kategori_receive = request.form["kategori_give"]
        place_receive = request.form["place_give"]
        deskripsi_receive = request.form["deskripsi_give"]
        
        doc = {
            'ID' : id_receive,
            "image"  : image_receive,
            "category" : kategori_receive,
            "name_place" : place_receive,
            "description" : deskripsi_receive,
        }
        db.destinasi.insert_one(doc)
        return jsonify({"result": "success", "msg": "Posting successful!"})

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