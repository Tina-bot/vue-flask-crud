from app import db

class Empleado(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    cargo = db.Column(db.String(100))
    salario = db.Column(db.Float)
    fecha_nacimiento = db.Column(db.Date)

    def __init__(self, nombre, apellido, edad, cargo, salario, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.cargo = cargo
        self.salario = salario
        self.fecha_nacimiento = fecha_nacimiento