





import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {'db': 'employee','host': 'localhost','port': 27017
}
db = MongoEngine()
db.init_app(app)




category = ('Ipledge to1', 'Ipledge to2', 'Ipledge to3', 'Ipledge to4')
class student(db.Document):
    name = db.StringField()
    DOB=db.StringField()
    email = db.StringField()
    mobaile=db.StringField()
    pincode=db.StringField()
    boolean_field_with_null = db.BooleanField(default=True, null=True)
    aadharcard=db.IntField()
    #selected_document=db.FileField()
    # nominator_identity_doc_number=db.IntField()
    
    
    nominator_identity_doc_number=db.IntField()
    
    nominee_name=db.StringField()
    nominee_DOB=db.StringField()
    nominee_mobile=db.StringField()
    nominee_email = db.StringField()
    nominee_pincode=db.StringField()
    award_category= db.StringField(max_length=50, choices=category)
    project_information= db.StringField()
    
    
    
    def to_json(self):
        return {"name": self.name,
                "DOB":self.DOB,
                "email": self.email,
                "mobaile":self.mobaile,
                "pincode":self.pincode,
                "Do have aadharcard":self.boolean_field_with_null,
                "Aadharcard Number":self.aadharcard,
                #"selected_document":self.selected_document,
                
                
                 "nominator_identity_doc_number":self. nominator_identity_doc_number,
                
                
                
                "nominee_name":self.nominee_name,
                "nominee_DOB":self.nominee_DOB,
                "nominee_mobile":self.nominee_mobile,
                "nominee_email":self.nominee_email,
                "nominee_pincode":self.nominee_pincode,
                "award_category":self.award_category,
                "project_information":self.project_information
                
                
                
                
                
                
                
                }

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
    user = student(name=record['name'],DOB=record["DOB"] ,email=record['email'],mobaile=record["mobaile"],pincode=record["pincode"],address=record["address"],message=record["message"],
                    nominator_identity_doc_number=record["nominator_identity_doc_number"], boolean_field_with_null=record["DO have Aadharcard"],
                    aadharcard=record["Aadharcard Number"], 
                    nominee_name=record['nominee_name'],
                    nominee_DOB=record["nominee_DOB"] ,
                    nominee_mobile=record["nominee_mobaile"],
                    nominee_email=record["nominee_email"],
                    nominee_pincode=record["nominee_pincode"],
                    award_category=record["award_category"],
                    project_information=record["project_information"]
                
                   )
    user.save()
    return jsonify(user.to_json())



if __name__=="__main__":
    app.run(debug=True)
