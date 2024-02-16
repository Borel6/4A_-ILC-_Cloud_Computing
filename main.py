from flask import Flask, render_template, request
import json 

import redis
r = redis.Redis(host='localhost', port=6379, db=0)


app = Flask(__name__)



resultats = {1 : 5}


@app.route("/display", methods=['GET'])
def get_result():
	if request.method == 'GET':
		return str((resultats.items()))
     
#addition
@app.route("/api/add/<A>/<B>", methods=["GET", "POST"])
def add(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        C = A + B 
        id = r.dbsize() + 1
        r.set(id, C) 
        resultats[id] = C

        return " a bien été ajouté au dictionnaire"


#soustraction
@app.route("/api/subs/<A>/<B>", methods=["GET", "POST"])
def subs(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        C = A - B 
        id = r.dbsize() + 1
        r.set(id, C) 

        resultats[id] = C

        return " a bien été ajouté au dictionnaire"
    
#division
@app.route("/api/div/<A>/<B>", methods=["GET", "POST"])
def div(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        if (B == 0) :
              return "division impossible"

        C = A - B 
        id = r.dbsize() + 1
        resultats[id] = C
        r.set(id, C) 


        return " a bien été ajouté au dictionnaire"
    
#multiplication
@app.route("/api/multi/<A>/<B>", methods=["GET", "POST"])
def multi(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        C = A * B 
        id = r.dbsize() + 1
        resultats[id] = C
        r.set(id, C) 


        return " a bien été ajouté au dictionnaire"

