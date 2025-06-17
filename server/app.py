from flask import Flask,make_response,request
from flask_migrate import Migrate
from models.pizza import Pizza,db
from models.restaurant import Restaurant,db
from models.restaurant_pizza import RestaurantPizza,db

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

migrate = Migrate(app, db)
