from sqlalchemy_serializer import SerializerMixin
from pizza import db

class Restaurant(db.Model,SerializerMixin):
      __tablename__='Restaurants'

      id=db.Column(db.Integer, primary_key=True)
      name=db.Column(db.String)
      address=db.Column(db.String)