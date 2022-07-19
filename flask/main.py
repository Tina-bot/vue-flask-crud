from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()

# creo la conexion a la base de datos con la configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql10506570:IGvdjzVpuY@sql10.freesqldatabase.com/sql10506570'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



CORS(app, resources={r"/*":{'origins':"*"}})

from route.empleado import empleado_router
app.register_blueprint(empleado_router)

if __name__ == '__main__':
    app.run(port=(os.getenv('PORT') if os.getenv('PORT') else 8000))