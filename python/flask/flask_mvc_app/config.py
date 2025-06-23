from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/flipkartdb'
app.config['SQLALCHEMY_ECHO'] = False
app.config['JWT_SECRET_KEY'] = "AJKSI@&$IHSJSY#*KSKKDK($DDKF$YJSJHJFHDJDFH"

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=1)   # 1 min
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(hours=8)    # 1 day


db = SQLAlchemy(app)
from flask_jwt_extended import *

jwt = JWTManager(app)  # Json Web Token