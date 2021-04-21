from flask import Flask, render_template, request, make_response, session
from DBHandler import DBHandler
from Donor import Donor
from User import User

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = "Hello World"

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/")
def signin():
    return render_template("signin.html")

@app.route("/verify", methods=["GET","POST"])
def verify():
    em = request.form["email"]
    pas = request.form["pass"]
    user = User("",em,pas)
    db = DBHandler(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    verified = db.verifyUser(user)
    if not verified:
        return render_template("signin.html",error="Wrong email or password")
    session["name"]=user.name
    session["email"]=user.email
    session["password"]=user.password
    return render_template("dashboard.html",name=session["name"])


@app.route("/register", methods=["GET","POST"])
def register():
    n = request.form["name"]
    em = request.form["email"]
    pas = request.form["pass"]
    session["name"]=n
    session["email"]=em
    session["password"]=pas
    user = User(n,em,pas)
    db = DBHandler(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    insert = db.insertUser(user)
    if insert is False:
        return render_template("signup.html",error="Invalid username or email")
    return render_template("dashboard.html",name=user.name)


@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    return render_template("dashboard.html",name=session["name"])

@app.route('/request')
def send_requet():
    return render_template("search.html",message="Request Sent")

@app.route('/addDonor')
def addDonor():
    return render_template('addDonor.html',name=session["name"])


@app.route('/logout')
def logout():
    session.clear()
    return render_template('signin.html')

@app.route('/donor', methods=["GET","POST"])
def registerDonor():
    n = request.form["name"]
    bg = request.form["blood_group"]
    ph = request.form["phone"]
    cn = request.form["cnic"]
    ct = request.form["city"]
    donor = Donor(n,bg,ph,cn,ct)
    db = DBHandler(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    insert = db.insertDonor(donor)
    if insert is False:
        return render_template("addDonor.html",error="Invalid Input")
    return render_template("dashboard.html",name=session["name"])
    
@app.route('/search',methods=["GET","POST"])
def search():
    db = DBHandler(app.config["DB_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    if request.method == "GET":
        return render_template('search.html', data={}, name=session["name"])
    elif request.method == "POST":
        blood_group = request.form["bg"]

        if blood_group !="":
            donorList = db.getAvailableDonors(blood_group)
        else:
            donorList = db.fetchAllDonors()
        return render_template('search.html', donorList = donorList, name=session["name"])

if __name__ == '__main__':
    app.run(debug=True)