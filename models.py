from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, Integer, String 

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

    with app.app_context():
        db.create_all()

class Form(db.Model):
    id = Column(Integer,primary_key=True)
    first_name = Column(String(),nullable=False)
    last_name =Column(String(),nullable=False)
    password = Column(Integer(),nullable=False)
    email  =Column(String(),nullable=False)

    def __init__(self,id,first_name,last_name,password,email):
        id         = self.id 
        first_name = self.first_name
        last_name  = self.last_name
        password   = self.password
        email      = self.email 

    def insert(self):
        db.session.add(self)
        db.session.commit()
        db.session.close()