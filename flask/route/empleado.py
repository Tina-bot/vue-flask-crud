from flask import jsonify, request, Blueprint
from marshmallow import ValidationError
from schemas.empleado import empleado_schema, empleados_schema
from models.Empleado import Empleado
from app import db

empleado_router = Blueprint('empleado', __name__)

@empleado_router.route('/empleados', methods=['GET'])
def get_empleados():
    all_empleados = Empleado.query.all()
    result = empleados_schema.dump(all_empleados)
    return jsonify(result)

@empleado_router.route('/empleados/<id>', methods=['GET'])
def get_empleado(id):
    empleado = Empleado.query.get(id)
    return empleado_schema.jsonify(empleado)

@empleado_router.route('/empleados', methods=['POST'])
def create_empleado():
    json_data = request.get_json()
    if not json_data:
        return {"message":"No hay data"},400
    try: 
        data= empleado_schema.load(json_data)
    except ValidationError as err :
        return err.messages, 422
    empleado = Empleado(
        nombre = data['nombre'], apellido = data['apellido'],
        edad = data['edad'], cargo = data['cargo'],
        salario= data['salario'], fecha_nacimiento = data['fecha_nacimiento']
    )
    db.session.add(empleado)
    db.session.commit()

    result = empleado_schema.dump(Empleado.query.get(empleado.id))

    return result

@empleado_router.route('/empleados/<id>', methods=['PUT'])
def update_empleado(id):
    empleado = Empleado.query.get(id)
    json_data = request.get_json()
    if not json_data:
        return {"message":"No hay data"},400
    try: 
        data= empleado_schema.load(json_data)
    except ValidationError as err :
        return err.messages, 422
    empleado.nombre = data['nombre']
    empleado.apellido = data['apellido']
    empleado.edad = data['edad']
    empleado.cargo = data['cargo']
    empleado.salario = data['salario']
    empleado.fecha_nacimiento = data['fecha_nacimiento']
    db.session.commit()

    result = empleado_schema.dump(Empleado.query.get(empleado.id))

    return result

@empleado_router.route('/empleados/<id>', methods=['DELETE'])
def delete_empleado(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()

    result = empleado_schema.dump(Empleado.query.get(empleado.id))

    return result

