from models.model import db
from passlib.hash import pbkdf2_sha256

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    email_address = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password = pbkdf2_sha256.hash(password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)
    
class Birthday(db.Model):
    __tablename__ = 'birthday'
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    day = db.Column(db.Integer, nullable=False)
    personal_data = db.relationship('User', back_populates='birthday')

class Personal_Data(db.Model):
    __tablename__ = 'personal_data'
    id = db.Column(db.Integer, primary_key=True)
    birthday_id = db.Column(db.Integer, db.ForeignKey('birthday.id'), nullable=False)
    birthday = db.relationship('Birthday', back_populates='personal_data')
    weight = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    bmi = db.Column(db.Float, nullable=False)
    does_exercise = db.Column(db.Boolean, nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=True)
    exercise = db.relationship('Exercise', back_populates='personal_data')
    sleep_time_id = db.Column(db.Integer, db.ForeignKey('sleep_time.id'), nullable=True)
    sleep_time = db.relationship('Sleep_Time', back_populates='personal_data')

    def set_bmi(self, weight, height):
        self.bmi = weight / (height * height) * 703

class Exercise(db.Model):
    __tablename__ = 'exercise'
    id = db.Column(db.Integer, primary_key=True)
    weekly_amt = db.Column(db.Integer, nullable=True)
    personal_data = db.relationship('Personal_Data', back_populates='exercise')
    exercise_type = db.relationship('Exercise_Type', back_populates='exercise')

class Exercise_Type(db.Model):
    __tablename__ = 'exercise_type'
    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    exercise = db.relationship('Exercise', back_populates='exercise_type')
    type = db.Column(db.String(50), nullable=False)
    hours = db.Column(db.Integer, nullable=False)

class Sleep_Time(db.Model):
    __tablename__ = 'sleep_time'
    id = db.Column(db.Integer, primary_key=True)
    personal_data = db.relationship('Personal_Data', back_populates='sleep_time')
    estimated_start_sleep = db.Column(db.Integer, nullable=False)
    estimated_end_sleep = db.Column(db.Integer, nullable=False)