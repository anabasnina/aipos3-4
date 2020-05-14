from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.DevelopementConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views
