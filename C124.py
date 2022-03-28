from distutils.log import error
from http.client import OK
import json
from tkinter.messagebox import YES
from flask import Flask,jsonify,request

app = Flask(__name__)
data = [
    {'contact':9820186757,
    'Name':'Raju',
    'id':1,
    'done':False},
     {'contact':9820186787,
    'Name':'Rahul',
    'id':2,
    'done':False}
]

@app.route('/A')

def rudra():
    return('hello')

@app.route('/add-data',methods = ['POST'])

def addTask():
    if not request.json:
        return jsonify({'status':'error','message':'please enter data'},400)

    contact = {
        'id':data[-1]['id']+1,
        'title':request.json['Name'],
        'desc':request.json.get('contact',''),
        'done':False
        }
    data.append(contact)
    return jsonify({"status":"success", "message": "Task added succesfully!"})

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : data
            })
app.run()


