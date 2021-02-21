from flask import Flask ,jsonify
from selenium import webdriver
import os
from casovi_scraper import login, get_info
app = Flask(__name__)

@app.route("/login")
def dojob():
    login()
    return jsonify({'response' : 'ok'}),200

@app.route('/getinfo/<token>')
def getinfo(token):
    try:
        result = get_info(token)
        return jsonify({'response' : result}),200
    except:
        return jsonify({'response' : token}),200
@app.route("/")
def index():
    return jsonify({'login': '/login'},{'getinfo':'/getlist/url'}),200

if __name__ == "__main__":
    app.run(debug=True)
    