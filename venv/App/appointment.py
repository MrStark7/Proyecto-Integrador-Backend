from .app import db

class Appointment(db.Model):
    __tablename__ = 'appointment'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    service_id = db.Column(db.Integer, nullable=False)

    def __init__(self, date, user_id, service_id):
        self.date = date
        self.user_id = user_id
        self.service_id = service_id
