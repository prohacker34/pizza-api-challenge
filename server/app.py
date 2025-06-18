from flask import Flask,make_response,request
from flask_migrate import Migrate
from flask_restful import Api,Resource
from models import db,Pizza,Restaurant,RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api=Api(app)

class PizzaEndpoint(Resource):
      def get(self):

          pizzas=[pizza.to_dict() for pizza in Pizza.query.all()]
          return make_response(pizzas,200)

class PizzaEndpointById(Resource):
      def get(self,id):
          pizza=Pizza.query.filter(Pizza.id==id).first()
          return make_response(pizza.to_dict(),200)

class RestaurantEndpoint(Resource):
      def get(self):
          restaurants=[restaurant.to_dict() for restaurant in Restaurant.query.all()]
          return make_response(restaurants,200)
class RestaurantEndpointById(Resource):
        def get(self,id):
            restaurant=Restaurant.query.filter(Restaurant.id==id).first()
            return make_response(restaurant.to_dict(),200)
class RestaurantEndpointDelete(Resource):
        def delete(self,id):

            db.session.delete(restaurant)
            db.session.commit()
            if restaurant:
                restaurant=Restaurant.query.filter(Restaurant.id==id).first()
                return make_response('204 no content')
            else:
                 return make_response({'eror':'Restaurant not found'})

class PostRestaurantPizza(Resource):
        def post(self):
             data = request.get_json()
             new_Rp= RestaurantPizza(
                 price=data['price'],
                 pizza_id=data['pizza_id'],
                 restaurant_id=data['restaurant_id']
             )
             db.session.add(new_Rp)
             db.session.commit()


api.add_resource(PizzaEndpoint,'/pizzas')
api.add_resource(PizzaEndpointById,'/pizzas/<int:id>')

api.add_resource(RestaurantEndpoint,'/restaurants')
api.add_resource(RestaurantEndpointById,'/restaurants/<int:id>')

api.add_resource(RestaurantEndpointDelete,'/restaurants/<int:id>/delete')
api.add_resource(PostRestaurantPizza,'/restaurant_pizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

