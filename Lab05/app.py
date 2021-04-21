from flask import Flask, render_template, request
from DBHandler import DBHandler
from Donor import Donor

app = Flask(__name__)
app.config.from_object("config")

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route('/addDonor')
def addDonor():
    return render_template('addDonor.html')

@app.route('/donor', methods=["GET","POST"])
def registerDonor():
    n = request.form["name"]
    bg = request.form["blood_group"]
    ph = request.form["phone"]
    cn = request.form["cnic"]
    ct = request.form["city"]
    donor = Donor(n,bg,ph,cn,ct)
    db = DBHandler(app.config["DB_IP"],app.config["DB_USER"],app.config["DB_PASSWORD"],app.config["DATABASE"])
    insert = db.insertRecord(donor)
    if insert is False:
        return render_template("failure.html")
    return render_template("success.html")
    
@app.route('/search',methods=["GET","POST"])
def search():
    db = DBHandler(app.config["DB_IP"], app.config["DB_USER"], app.config["DB_PASSWORD"], app.config["DATABASE"])
    if request.method == "GET":
        return render_template('search.html', data={})
    elif request.method == "POST":
        name = request.form["name"]
        blood_group = request.form["bg"]
        phone = request.form["phn"]
        city = request.form["ct"]

        hasName= False
        hasPhone=False
        hasBG = False
        hasCity =False

        # generating Dynamic query for Filtering
        query = "select * from donors where "
        if(not name == ""):
            query+=f" name like \"%{name}%\""
            hasName = True
        if(not phone == ""):
            hasPhone= True
            if hasBG or hasCity or hasName:
                query = query+f" and phone like \"%{phone}%\"%"
            else:
                query = query+f" phone like \"%{phone}%\""
        if(not blood_group == ""):
            hasBG = True
            if hasCity or hasPhone or hasName:
                query = query+f" and blood_group = \"{blood_group}\""
            else:
                query = query+f" blood_group = \"{blood_group}\""
        if(not city == ""):
            if hasBG or hasPhone or hasName:
                query = query+f" and city = \"{city}\""
            else:
                query = query+f" city = \"{city}\""
        if(name == "" and phone == "" and blood_group == "" and city == ""):
            query = "SELECT * FROM donors"

        donorList = db.searchfor(query)
        return render_template('search.html', query = query ,donorList = donorList)

if __name__ == '__main__':
    app.run(debug=True)