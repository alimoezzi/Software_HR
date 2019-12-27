import flask_praetorian
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
guard = flask_praetorian.Praetorian()