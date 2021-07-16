from flask import Flask,jsonify,request
app=Flask(__name__)
List=[
    {
        'id':1,
        'Name':u'Rohan',
        'Contact':u'6624020301',
        'done':False
    },
    {
        'id':2,
        'Name':u'Bryan',
        'Contact':u'6628435430',
        'done':False
    }
]
@app.route("/")
def hello_world():
    return "hello world!"
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    contact={
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    List.append(contact)
    return jsonify({
        "status":"success",
        "message":"contact added"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":List
    })
if(__name__=="__main__"):
    app.run(debug=True)