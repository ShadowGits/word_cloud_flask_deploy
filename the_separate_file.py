from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 
from flask_sqlalchemy import SQLAlchemy

  
# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

#db uri
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:losinghimwasblue@localhost/TheWordCloudDB'

db = SQLAlchemy(app)

class Image(db.Model):
    __tablename__="Images"
    id = db.Column(db.Integer, primary_key=True)
    encoded_image= db.Column(db.String,unique=True)

    def __init__(self,encoded_image):
        self.encoded_image=encoded_image
    def __repr__(self):
        return self.encoded_image
    
  
# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class Hello(Resource): 
  
    # corresponds to the GET request. 
    # this function is called whenever there 
    # is a GET request for this resource 
    def get(self): 
  
        return jsonify({'message': 'hello world'}) 
  
    # Corresponds to POST request 
    def post(self): 
          
        data = request.get_json()     # status code 
        return jsonify({'data': data}), 201
  
  
# another resource to calculate the square of a number 
class Square(Resource): 
  
    def get(self, num): 
  
        return jsonify({'square': num**2}) 
  
  
# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(Square, '/square/<int:num>') 
  
  
# driver function 
if __name__ == '__main__': 
  
    app.run(debug = True) 
