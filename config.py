# import OS module
import os

#creation of base directory for application
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents\chicodes_sept2020\week_5\week5HW


#Config Class
#Configure the database (when we have one) AND configure the 
#secret key for the encryption of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
