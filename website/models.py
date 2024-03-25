from . import db
#from flask_login import UserMixin

class Vaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vaccin_date = db.Column(db.DateTime)
    vaccin_number = db.Column(db.Integer)
    manufacturer = db.Column(db.String(150))
    member_id = db.Column(db.Integer, db.ForeignKey('corona.member_id'))

class Corona(db.Model):
    positive_date = db.Column(db.String(10))
    recovery_date = db.Column(db.String(10))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), primary_key=True)
    vaccination = db.relationship('Vaccination')

class Member(db.Model):
    full_name = db.Column(db.String(150))
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(150))
    date = db.Column(db.DateTime)
    phone = db.Column(db.Integer)
    mobile_phone = db.Column(db.Integer, unique=True)
    corona = db.relationship('Corona', uselist=False)