
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {'db': 'employee','host': 'localhost','port': 27017
}
db = MongoEngine()
db.init_app(app)

class student(db.Document):
    name = db.StringField()
    DOB=db.StringField()
    email = db.StringField()
    mobaile=db.StringField()
    pincode=db.StringField()
    address=db.StringField()
    message=db.StringField()
    
    
    def to_json(self):
        return {"name": self.name,
                "DOB":self.DOB,
                "email": self.email,
                "mobaile":self.mobaile,
                "pincode":self.pincode,
                "address":self.address,
                "meassage":self.message}

@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('name')
    user = student.objects(name=name).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(user.to_json())




@app.route('/addrecord', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    user = student(name=record['name'],DOB=record["DOB"] ,email=record['email'],mobaile=record["mobaile"],pincode=record["pincode"],address=record["address"],message=record["message"])
    user.save()
    return jsonify(user.to_json())



if __name__=="__main__":
    app.run(debug=True)
