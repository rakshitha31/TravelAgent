# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 11:28:49 2019

@author: K.S.LOHITH
"""

import cgi,cgitb
import pyrebase
from flask_cors import CORS
import json
import random
from flask import Flask , request , render_template, redirect , session , flash
from datetime import date
app = Flask(__name__,template_folder='templates')
CORS(app)
app.secret_key = 'thatswhatshesaid'
config = {
    "apiKey": "AIzaSyChod2N_h8zx7jW-twHnVOSO_Sn_-DuWPQ",
    "authDomain": "travelinstyle-534e6.firebaseapp.com",
    "databaseURL": "https://travelinstyle-534e6.firebaseio.com",
    "projectId": "travelinstyle-534e6",
    "storageBucket": "",
    "messagingSenderId": "1009799677476",
    "appId": "1:1009799677476:web:0809f2458858f10d"
        }
firebase = pyrebase.initialize_app(config)

db = firebase.database()

@app.route("/",methods=['GET','POST'])
def start():
    return render_template("Login_main.html")

@app.route("/verifyagent",methods=['GET','POST'])
def verify():
    usern=request.form['username']
    password=request.form['pass']
    users = db.child("travel_agents").get()
    for user in users.each():
        print(user.key())
        details = (user.val())
        myinnerdetails = (list(details.values()))
        print(myinnerdetails)
        for name in (myinnerdetails):
            user1 = (name['username'])
            pass1 = (name['password'])
            if usern == user1 and pass1 == password :
                flash("Login successful")
                return render_template("insertdata.html")
            else:
                return render_template("wrong_password.html")
    return "true"
    
    
@app.route("/register",methods=['GET','POST'])
def register():
    return render_template("register.html")

@app.route("/transfer",methods=['GET','POST'])
def transfer():
    if(request.method == 'POST'):  
    
            req_data=request.get_data()
            #name=req_data['name']
            req_data=req_data.decode()
            y = json.loads(req_data)
            cloudWrite(y)
            
            
            return 'done'
            
    else:
        return 'fail'
    
def cloudWrite(y):
    name=y['name']
    email=y['email']
    mobile=y['mobile']
    departure = y['depdate']
    arrival = y['arrdate']
    room = y['rooms']
    adults = y['adults']
    children = y['children']
    hotel = y['hotel']
    
    db.child("booking_details").child(name).push({"name":name,"email":email,"contact":mobile,"departure":departure,"arrival":arrival,"room":room,"Adults":adults,"Children":children,"hotel":hotel})
    
    

@app.route("/addtravelagents",methods=['GET','POST'])
def add():
    agency = request.form['AgencyName']
    email = request.form['email']
    user = request.form['username']
    password = request.form['pass']
    db.child("travel_agents").child(agency).push({"agency":agency,"email":email,"username":user,"password":password})
    flash("You were successfully registered")
    return render_template("Login_main.html")
        
    
@app.route("/submit",methods=['GET','POST'])
def submit():
    name="lohith"
    email="kslohith1729@gmail.com"
    message="welcome"
    db.child("travel_agents").child(name).push({"name":name,"email":email,"message":message})
    return "true"

    
if __name__ == "__main__":
    app.run()


