from flask_restful import Resource, reqparse
from models.reservationModel import ReservationModel
from models.eventModel import EventModel
default_help = 'This field cannot be blank'

_RESERVATION_PARSER = reqparse.RequestParser()
_RESERVATION_PARSER.add_argument('title', type=str, required=True, help=default_help)



class Reservation(Resource):
    def get(self, code):
        reservation = ReservationModel.find_by_code(code)
        if reservation:
            return reservation.json()
        return {'message': 'Reservation not found'}, 404
    
    def put(self, code):
        """ Cancelling a reservation """
        try:
            reservation = ReservationModel.find_by_code(code)
            if(reservation.checkIfCanBeCancelled()):
                reservation.cancel()
                return {'message': 'Reservation cancelled'}, 200
            else:
                return {'message': 'Reservation cannot be cancelled'}, 400
        except:
            return {'message': 'could not find reservation'},404 


class ReservationCreate(Resource):
    def post(self):
        data = _RESERVATION_PARSER.parse_args()
        if EventModel.find_by_title(data['title']) is None:
            return {'message': 'Event not found'}, 404
        reservation = ReservationModel(**data)
        try:
            reservation.save_to_db()
        except:
            return {'message': 'An error occurred while creating the reservation.'}, 500
        return reservation.json(), 201