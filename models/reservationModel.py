from db import db
import string
import random

class ReservationModel(db.Model):
    __tablename__   = 'reservations'
    
    id_reservation  = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(80))
    startDate       = db.Column(db.String(80))
    endDate         = db.Column(db.String(80))
    active          = db.Column(db.Boolean)
    code            = db.Column(db.String(80))
    
    def __init__(self, title, startDate, endDate, active=True):
        self.title       = title
        self.startDate   = startDate
        self.endDate     = endDate
        self.active      = active
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
    
    def json(self):
        return {'title': self.title, 
                'startDate': self.startDate, 
                'endDate': self.endDate, 
                'active': self.active, 
                'code': self.code
                }
    
    @classmethod
    def find_by_id(cls, _id)-> object:
        return cls.query.filter_by(id_reservation=_id).first()
    
    @classmethod
    def find_by_code(cls, code)-> object:
        return cls.query.filter_by(code=code).first()