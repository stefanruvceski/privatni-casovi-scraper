from flask import Flask ,jsonify,render_template,request
from selenium import webdriver
import os
from casovi_scraper import login, get_info
app = Flask(__name__)



@app.route("/login",methods = ['POST', 'GET'])
def login():
    #try:
        email = request.form['email']
        login(email)
        return render_template("token.html")
    #except:
        #return render_template("error.html",err='Doslo je do greske prilikom prijave')

@app.route("/getstats",methods = ['POST', 'GET'])
def getinfo():
    try:
        token = request.form['token']
        my_name,stats = get_info(token)
        return render_template("index.html", stats=stats, my_name=my_name)
    except:
        return render_template("error.html",err='Doslo je do greske prilikom kreiranja statistike')
    
@app.route("/")
def index():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
    