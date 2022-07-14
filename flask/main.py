from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()

# creo la conexion a la base de datos con la configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10506570:IGvdjzVpuY@sql10.freesqldatabase.com/sql10506570'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



CORS(app, resources={r"/*":{'origins':"*"}})


if __name__ == '__main__':
    from route.empleado import empleado_router
    app.register_blueprint(empleado_router)
    app.run(debug=True)
    