
import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {'db': 'employee','host': 'localhost','port': 27017
}
db = MongoEngine()
db.init_app(app)



organaistion=("org1","org2","org3","org4","org5","org6")
industry=("IT","com","civil","mech","sofwere","devlop")
category = ('Ipledge to1', 'Ipledge to2', 'Ipledge to3', 'Ipledge to4')
class nomine(db.Document):
    organaistion=db.StringField()
    organaistion_name=db.StringField()
    industry=db.StringField()
    DOB_incorportion=db.StringField()
    
    

    name = db.StringField()
    DOB=db.StringField()
    email = db.StringField()
    mobile=db.StringField()
    pincode=db.StringField()
    boolean_field_with_null = db.BooleanField(default=True, null=True)
    aadharcard=db.StringField()
    selected_document=db.StringField()
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
        return {"Type organaistion":self. organaistion,"organaistion_name":self.organaistion_name,"industry":self.industry,"Date of incorportion":self.DOB_incorportion,
                "name": self.name,
                "DOB":self.DOB,
                "email": self.email,
                "mobile":self.mobile,
                "pincode":self.pincode,
                "Do have aadharcard":self.boolean_field_with_null,
                "Aadharcard Number":self.aadharcard,
                "selected_document":self.selected_document,
                
                
                 "nominator_identity_doc_number":self. nominator_identity_doc_number,
                
                
                
                "nominee_name":self.nominee_name,
                "nominee_DOB":self.nominee_DOB,
                "nominee_mobile":self.nominee_mobile,
                "nominee_email":self.nominee_email,
                "nominee_pincode":self.nominee_pincode,
                "award_category":self.award_category,
                "project_information":self.project_information
                }


@app.route('/addrecord', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    user =nomine(organaistion=record["Type organaistion"],organaistion_name=record["organaistion_name"],industry=record["industry"],DOB_incorportion=record["Date of incorportion"],
                 name=record['name'],
                 DOB=record["DOB"],
                 email=record['email'],
                 mobile=record["mobile"],
                 pincode=record["pincode"],
                 boolean_field_with_null=record["Do have aadharcard"],
                 aadharcard=record["Aadharcard Number"], 
                 selected_document=record["selected_document"],
                 
                 
                 nominator_identity_doc_number=record["nominator_identity_doc_number"], 
                 nominee_name=record['nominee_name'],
                 nominee_DOB=record["nominee_DOB"] ,
                 nominee_mobile=record["nominee_mobile"],
                 nominee_email=record["nominee_email"],
                 nominee_pincode=record["nominee_pincode"],
                 award_category=record["award_category"],
                 project_information=record["project_information"]
                 
                 )
    user.save()
    return jsonify(user.to_json())



if __name__=="__main__":
    app.run(debug=True)
