from app import db

class Assessment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    moduleCode = db.Column(db.String(9), index=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(500))
    dateTime = db.Column(db.DateTime)
    completion = db.Column(db.Boolean, default=False)