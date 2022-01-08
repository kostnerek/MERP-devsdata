from flask_restful import Resource, reqparse
from models.eventModel import EventModel
import werkzeug
from flask import send_file

default_help = 'This field cannot be blank'

_EVENT_PARSER = reqparse.RequestParser()
_EVENT_PARSER.add_argument('title', type=str, required=True, help=default_help)
_EVENT_PARSER.add_argument('startDate', type=str, required=True, help=default_help)
_EVENT_PARSER.add_argument('endDate', type=str, required=True, help=default_help)

_IMAGE_PARSER = reqparse.RequestParser()
_IMAGE_PARSER.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help=default_help)

class Event(Resource):
    def get(self):
        all_events = EventModel.find_all()
        parsed_events = [event.json() for event in all_events]
        return {'events': parsed_events}, 200
            
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


class EventThumbnail(Resource):
    def post(self, title):
        try:
            event = EventModel.find_by_title(title)
        except:
            return {'message': 'You cannot add thumbnail to non existing event'}, 400
            
        data = _IMAGE_PARSER.parse_args()
        img = data['image']
        img.save(f'frontend/public/thumbnails/{title}.jpg')
        event.set_thumbnail(f'/thumbnails/{title}.jpg')
        return {'message': 'Thumbnail added successfully'}, 201
    
    def get(self, title):
        try:
            event = EventModel.find_by_title(title)
        except:
            return {'message': 'You cannot get thumbnail of non existing event'}, 400
        return send_file(event.thumbnail, mimetype='image/jpeg')

