from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'UserData'
app.config['MONGO_URI'] = 

db = MongoEngine()
db.init_app(app)

class User(db.Document):
    category = db.stringField()
    amount = db.stringField()

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/store', methods=['POST'])
def post_entry():
    category = request.json['category']
    amount = request.json['amount']
    entry_id = 





  name = request.json['name']
  distance = request.json['distance']
  star_id = star.insert({'name': name, 'distance': distance})
  new_star = star.find_one({'_id': star_id })
  output = {'name' : new_star['name'], 'distance' : new_star['distance']}
  return jsonify({'result' : output})