from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patients'
    patient_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    given_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(1), nullable=False)  # M or F
    dob = db.Column(db.Date, nullable=False)
    current_location = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(20), nullable=False)
    origin_province = db.Column(db.String(50), nullable=True)
    clinic_referral_source = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
