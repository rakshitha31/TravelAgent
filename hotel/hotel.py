# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:32:29 2019

@author: K.S.LOHITH
"""

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
import smtplib
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

def stream_handler(message):
    #print(message["event"]) 
    #print(message["path"]) 
    print(message["data"])
my_stream = db.child("booking_details").stream(stream_handler)

    
if __name__ == "__main__":
    app.run()


