from flask import Flask
from flask_restful import Api, Resource
from db import db

from resources.ReservationResource import Reservation, ReservationCreate
from resources.EventResource import EventCreate, EventThumbnail

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Reservation, '/reservation/<string:code>')
api.add_resource(ReservationCreate, '/reservation/create')

api.add_resource(EventCreate, '/event/create')
api.add_resource(EventThumbnail, '/event/thumbnail/<string:title>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)