# Creates the application object as an instance of class Flask


from flask import Flask
from config import Config

app = Flask(__name__)

# using Config class from ./config.py
app.config.from_object(Config)

# The routes module is imported at the bottom and not at the top of the script
# as it is always done. The bottom import is a workaround to circular imports,
# a common problem with Flask applications.
from app import routes, models, errors
