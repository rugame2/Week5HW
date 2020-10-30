from flask import Flask

#import the config object
from config import Config

#import for the SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

#Import the Migrate Oject
from flask_migrate import Migrate

# Import for the flask Login Module
from flask_login import LoginManager

app = Flask(__name__)
# Complete the Config cycle to our own Flask App
# And give access to our database (when we have one)
# along with our Secret Key
app.config.from_object(Config)

#Init the database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app,db)

# Login Config - Init  for the LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Specifies what page to load for non authenticated users

#Won't create the tables if this line is not present
from avengers import routes,models