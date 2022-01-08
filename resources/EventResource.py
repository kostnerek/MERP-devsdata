from flask_restful import Resource, reqparse
from models.eventModel import EventModel

default_help = 'This field cannot be blank'

_EVENT_PARSER = reqparse.RequestParser()
_EVENT_PARSER.add_argument('title', type=str, required=True, help=default_help)
_EVENT_PARSER.add_argument('startDate', type=str, required=True, help=default_help)
_EVENT_PARSER.add_argument('endDate', type=str, required=True, help=default_help)

class EventCreate(Resource):
    def post(self):
        data = _EVENT_PARSER.parse_args()
        if EventModel.find_by_title(data['title']):
            return {'message': 'Event with this name already exists'}, 400
        
        event = EventModel(**data)
        try:
            event.save_to_db()
        except:
            return {'message': 'An error occurred while creating the event.'}, 500
        return event.json(), 201