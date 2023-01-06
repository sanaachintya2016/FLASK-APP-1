from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [{
    'id': 1,
    'contact': u'9865327489',
    'name': u'Dipa',
    'done': False
},{
    'id': 2,
    'contact': u'9765632215',
    'name': u'Shubham',
    'description': False
}]

@app.route("/add-data",methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide a data"
        },400)

    contacts = {
    'id':   tasks[-1]['id']+1,
    'name': request.json('name'),
    'contact': request.json('contact',""),
    'done': False
    }

    tasks.append(contacts)
    return jsonify({
            "status": "success",
            "message": "added successfully" 
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data": tasks
    })
if(__name__ == "__main__"):
    app.run(debug = True)