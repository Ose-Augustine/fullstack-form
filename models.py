from flask_sqlalchemy import SQLAlchemy 
import os 
from sqlalchemy import Column, Integer, String 
from flask_migrate import Migrate

database_name = "fullstacks"
database_path = "postgresql://{}:{}@{}/{}".format(
    "augustine","bahdman","localhost:5432",database_name
)

db = SQLAlchemy()

def setup_db(app,database_path=database_path):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    app.config['SQLALCHEMY_DATABASE_URI']=database_path
    app.config['SECRET_KEY']='bahdest'
    db.init_app(app)
    migrate = Migrate(app,db)

    with app.app_context():
        db.create_all()

class Person(db.Model):
    __tablename__ ='persons'
    id         = Column(Integer,primary_key=True,nullable=False)
    first_name = Column(String(),nullable=False)
    last_name  = Column(String(),nullable=False)
    password   = Column(String(),nullable=False) 
    confirm    = Column(String(),nullable=False)
    email      = Column(String(),nullable=True)


    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def reverse(self):
        db.session.rollback()