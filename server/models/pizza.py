from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Pizza(db.Model,SerializerMixin):
    __tablename__='pizzas'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    ingredients=db.Column(db.String)