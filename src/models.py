import datetime
from flask_sqlalchemy import SQLAlchemy


class Usuario(db.Model):
	idUsuario = db.Column(db.Integer,primary_key = True)
	usuario = db.Column(db.String(20),unique = True)
	password =  db.Column(db.String(20))
	nombre = db.Column(db.String(100))
	activo = db.Column(db.String(1), default = 'S')
	hora_alta = db.Column(db.DateTime,default = datetime.datetime.now)
	hora_baja = db.Column(db.DateTime, default = '1900-01-01')



