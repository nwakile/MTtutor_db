from flask_app import app
from app import User, Qb, Subject, Performance
import os

PATH = os.path.dirname(__file__)
DATAPATH = os.path.join(PATH, "data", "qb.db")

Qb.dbpath = DATAPATH
User.dbpath = DATAPATH
Subject.dbpath = DATAPATH
Performance.dbpath = DATAPATH


app.run(debug=True)