from db import db

class EventModel(db.Model):
    __tablename__   = 'events'
    
    id_event  = db.Column(db.Integer, primary_key=True)
    title           = db.Column(db.String(80))
    startDate       = db.Column(db.String(80))
    endDate         = db.Column(db.String(80))
    thumbnail       = db.Column(db.String(80))
    
    def __init__(self, title, startDate, endDate):
        self.title       = title
        self.startDate   = startDate
        self.endDate     = endDate
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
    def set_thumbnail(self, thumbnail):
        self.thumbnail = thumbnail
        self.save_to_db()
    
    def json(self):
        return {
                'title': self.title, 
                'startDate': self.startDate, 
                'endDate': self.endDate,
                'thumbnail': self.thumbnail
                }
    
    @classmethod
    def find_by_id(cls, _id)-> object:
        return cls.query.filter_by(id_reservation=_id).first()
    @classmethod
    def find_by_title(cls, title)-> object:
        return cls.query.filter_by(title=title).first()