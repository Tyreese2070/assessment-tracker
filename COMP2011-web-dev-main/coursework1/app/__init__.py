from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'chicken'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views
from app import models