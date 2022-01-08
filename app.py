from flask import Flask
from flask_cors import CORS
from flask_restful import Api, Resource
from db import db

from resources.ReservationResource import Reservation, ReservationCreate
from resources.EventResource import Event, EventThumbnail

from create_example_events import create_example_events
import os;os.mkdir("frontend/public/thubmnails")


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    #create_example_events()


api.add_resource(Reservation, '/reservation/<string:code>')
api.add_resource(ReservationCreate, '/reservation/create')

api.add_resource(Event, '/event')
api.add_resource(EventThumbnail, '/event/thumbnail/<string:title>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)