from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db,PdfDocument
from datetime import datetime
from datetime import timedelta
from flask_cors import CORS


app = Flask(__name__)


CORS(app)
# migration initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mpesadb_user:ef5RyMB1NuZcnxoWWgaxE4dePY2HQRc6@dpg-d1kdgu7diees73ec8be0-a.oregon-postgres.render.com/mpesadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)


# imports functions from views
from parser import *

app.register_blueprint(upload_bp)
app.register_blueprint(summary_bp)
app.register_blueprint(extract_bp)
app.register_blueprint(fetching_bp)



if __name__ == '__main__':
    app.run(debug=True)