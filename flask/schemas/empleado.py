from flask_marshmallow import Schema

class EmpleadoSchema(Schema):
    class Meta:
        fields = ('id', 'nombre', 'apellido', 'edad', 'cargo', 'salario', 'fecha_nacimiento')

empleado_schema = EmpleadoSchema() #crea un objeto de tipo EmpleadoSchema
empleados_schema = EmpleadoSchema(many=True) #crea lista de empleados