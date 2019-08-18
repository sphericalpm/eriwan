# Creates the application object as an instance of class Flask


from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config


app = Flask(__name__)

# using Config class from ./config.py
app.config.from_object(Config)

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# The routes module is imported at the bottom and not at the top of the script
# as it is always done. The bottom import is a workaround to circular imports,
# a common problem with Flask applications.
from app import routes, models
import atexit
from app.parser import parse_anekdot
from apscheduler.schedulers.background import BackgroundScheduler

def scheduler_parser():

    parse_anekdot()

scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduler_parser, trigger="interval", hour=Config.PARSE_TIME_HOURS)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())
