from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Usuarios(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    nombre = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    contrasenia = db.Column(db.String(255), nullable=False) 
    rol = db.Column(db.String(100), nullable=False) 
    created_date = db.Column(db.DateTime, default=datetime.datetime.now) 