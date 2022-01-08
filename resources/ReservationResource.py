from flask_restful import Resource, reqparse
from models.reservationModel import ReservationModel

default_help = 'This field cannot be blank'

_RESERVATION_PARSER = reqparse.RequestParser()
_RESERVATION_PARSER.add_argument('title', type=str, required=True, help=default_help)
_RESERVATION_PARSER.add_argument('startDate', type=str, required=True, help=default_help)
_RESERVATION_PARSER.add_argument('endDate', type=str, required=True, help=default_help)


class Reservation(Resource):
    def get(self, code):
        reservation = ReservationModel.find_by_code(code)
        if reservation:
            return reservation.json()
        return {'message': 'Reservation not found'}, 404
    
    def put(self, code):
        try:
            reservation = ReservationModel.find_by_code(code)
            reservation.active = False
            reservation.save_to_db()
            return {'message': 'Reservation cancelled'},200
        except:
            return {'message': 'An error occurred'},500


class ReservationCreate(Resource):
    def post(self):
        data = _RESERVATION_PARSER.parse_args()
        print(data)
        reservation = ReservationModel(**data)
        try:
            reservation.save_to_db()
        except:
            return {'message': 'An error occurred while creating the reservation.'}, 500
        return reservation.json(), 201