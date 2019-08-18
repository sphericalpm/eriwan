from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from config import Config

app = Flask(__name__)

# using Config class from ./config.py
app.config.from_object(Config)

# database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# authorization
login_manager = LoginManager(app)

#styles
bootstrap = Bootstrap(app)

# The routes module is imported at the bottom and not at the top of the script
# as it is always done. The bottom import is a workaround to circular imports,
# a common problem with Flask applications.
from app import routes, models, errors
