from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/atut22'

db = SQLAlchemy(app)

@app.before_first_request
def create_all():
    db.create_all()
