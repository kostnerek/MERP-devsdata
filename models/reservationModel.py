from db import db
import string
import random
import datetime
from models.eventModel import EventModel
class ReservationModel(db.Model):
    __tablename__   = 'reservations'
    
    id_reservation  = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(80))
    active          = db.Column(db.Boolean)
    code            = db.Column(db.String(80))
    
    def __init__(self, title):
        self.title       = title
        self.active      = True
        self.code        = self.generate_code()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def generate_code(self):
        code=''
        for x in range(6):
            code += random.choice(string.ascii_letters[26:])
        
        if ReservationModel.find_by_code(code):
            return self.generate_code()
        else:
            return code
    
    def checkIfCanBeCancelled(self):
        
        event = EventModel.find_by_title(self.title)

        dateStart = datetime.datetime.strptime(event.startDate, "%Y-%m-%dT%H:%M:%S")
        dateEnd = datetime.datetime.strptime(event.endDate,   "%Y-%m-%dT%H:%M:%S")

        timeDiff = dateEnd - dateStart

        if(timeDiff>datetime.timedelta(days=2)):
            if(dateStart-datetime.datetime.now()>datetime.timedelta(days=2)):
                return True
        return False
    
    def cancel(self):
        self.active = False
        self.save_to_db()
    
    def json(self):
        return {'title': self.title,
                'active': self.active, 
                'code': self.code
                }
    
    @classmethod
    def find_by_id(cls, _id)-> object:
        return cls.query.filter_by(id_reservation=_id).first()
    
    @classmethod
    def find_by_code(cls, code)-> object:
        return cls.query.filter_by(code=code).first()