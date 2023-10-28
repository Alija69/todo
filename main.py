from flask import jsonify,json,request, jsonify, make_response
from bson.objectid import ObjectId
from bson import json_util
from db import collection
from app import app

def parse_json(data):
    return json.loads(json_util.dumps(data))        
        
@app.route('/todo', methods=['GET','POST'])
def create_todo(): 
    try:
        if request.method == 'POST':
            data = request.get_json()
            create = collection.insert_one(data)
            return make_response(jsonify({"msg": "New todo created."}), 201)
        todos = collection.find()    
        return make_response(jsonify({"todo": parse_json(todos)}), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"msg":"an error occured try after some time."}),500)


@app.route('/todo/<id>', methods=['GET','DELETE','PUT'])
def alter_todo(id): 
    try:
        if request.method == 'GET':
            todo =  collection.find_one({"_id": ObjectId(id)})
            return make_response(jsonify({"todo": parse_json(todo)}), 200)
        elif request.method == 'PUT':
            data = request.get_json()
            todo = collection.update_one({'_id':ObjectId(id)}, {"$set": data}, upsert=False)
            return make_response(jsonify({"msg":"Updated successfully."}),200)
        elif request.method == 'DELETE' :
            collection.delete_one({'_id':ObjectId(id)})
            return make_response(jsonify({"msg" : "Deleted successfully.."}),200)
    except Exception as e:
        print(e)
        return make_response(jsonify({"msg":"an error occured try after some time."}),500)
   