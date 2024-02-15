from flask import Flask, render_template, request
from datetime import datetime
from datetime import timedelta
import csv
from io import StringIO

import json 

app = Flask(__name__)



resultats = {1 : 5}


#addition
@app.route("/add/<A>/<B>", methods=["GET", "POST"])
def add(A,B):
    if request.method == "GET":

        C = A + B 
        id = len(resultats) + 1
        resultats[id] = C

        return " a bien été ajouté au dictionnaire"


#soustraction
@app.route("/subs/<A>/<B>", methods=["GET", "POST"])
def subs(A,B):
    if request.method == "GET":

        C = A - B 
        id = len(resultats) + 1
        resultats[id] = C

        return " a bien été ajouté au dictionnaire"
    
#division
@app.route("/div/<A>/<B>", methods=["GET", "POST"])
def div(A,B):
    if request.method == "GET":
        if (B == 0) :
              return "division impossible"

        C = A - B 
        id = len(resultats) + 1
        resultats[id] = C

        return " a bien été ajouté au dictionnaire"
    
#multiplication
@app.route("/multi/<A>/<B>", methods=["GET", "POST"])
def multi(A,B):
    if request.method == "GET":

        C = A * B 
        id = len(resultats) + 1
        resultats[id] = C

        return " a bien été ajouté au dictionnaire"

