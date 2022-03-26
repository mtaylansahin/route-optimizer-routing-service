import resource
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, age):
        return {"name": name, "age": age}

api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")

if __name__=='__main__':
    app.run(debug=True)