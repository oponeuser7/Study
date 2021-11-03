from flask import Flask
from flask_restx import Resource, Api
import pymongo

app = Flask(__name__)
api = Api(app)
conn = pymongo.MongoClient("localhost", 27017)
db = conn.test
col = db.members

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        col = db.members
        people = {
            "이름" : "홍길동",
            "나이" :30,
            "별명" : "의적"
        }
        col.insert(people)
        return {'hello': 'world'}


