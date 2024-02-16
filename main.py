from flask import Flask, render_template, request
import json 

import redis

#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='calculs')



r = redis.Redis(host='localhost', port=6379, db=0)
app = Flask(__name__)



@app.route("/result/<res>", methods=["GET", "POST"])
def get_result(res):
	if request.method == 'GET':
            r.get(res)
            return res
     
#addition
@app.route("/api/add/<A>/<B>", methods=["GET", "POST"])
def add(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        id = r.dbsize()() + 1
        id = "calc" + str(id)
        data = {
        "id": id,
        "message": {
            "op": "add",
            "numA": A,
            "numB": B
            }
            }
        json_data = json.dumps(data)
        

        channel.basic_publish(exchange='',
                        routing_key='calculs',
                      body=json_data)
                      
        print(" [x] Sent 'Hello World!'")
        connection.close()

        return id 


#soustraction
@app.route("/api/subs/<A>/<B>", methods=["GET", "POST"])
def subs(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        id = r.dbsize() + 1
        id = "calc" + str(id)
        data = {
        "id": id,
        "message": {
            "op": "subs",
            "numA": A,
            "numB": B
            }
            }
        json_data = json.dumps(data)
        

        channel.basic_publish(exchange='',
                        routing_key='calculs',
                      body=json_data)
                      
        print(" [x] Sent 'Hello World!'")

        return id 
    
#division
@app.route("/api/div/<A>/<B>", methods=["GET", "POST"])
def div(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        if (B == 0) :
              return "division impossible"

        id = r.dbsize() + 1
        id = "calc" + str(id)
        data = {
        "id": id,
        "message": {
            "op": "multi",
            "numA": A,
            "numB": B
            }
            }
        json_data = json.dumps(data)
        

        channel.basic_publish(exchange='',
                        routing_key='calculs',
                      body=json_data)
                      
        print(" [x] Sent 'Hello World!'")

        return id 
    
#multiplication
@app.route("/api/multi/<A>/<B>", methods=["GET", "POST"])
def multi(A,B):
    if request.method == "GET":
        A = int(A)
        B = int(B)
        id = r.dbsize() + 1
        id = "calc" + str(id)
        data = {
        "id": id,
        "message": {
            "op": "multi",
            "numA": A,
            "numB": B
            }
            }
        json_data = json.dumps(data)
        

        return " a bien été ajouté au dictionnaire"

