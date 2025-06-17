from sqlalchemy_serializer import SerializerMixin
from pizza import db

class RestaurantPizza(db.Model,SerializerMixin):
      __tablename__='RestaurantPizzas'

      id=db.Column(db.Integer,primary_key=True)
      price=db.Column(db.Integer)
      restaurant=db.Column(db.Integer)
      pizza_id=db.Column(db.Integer)



