from models import Pizza,Restaurant,RestaurantPizza,db
from app import app

with app.app_context():
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()

    pizzas=[]

    peperoni = Pizza(name='peperoni', ingredients='garlic')
    mushroom = Pizza(name='mushroom', ingredients='hot sauce')
    pizzas.append(peperoni)
    pizzas.append(mushroom)

    db.session.add_all([peperoni, mushroom])
    db.session.commit()

    restaurants=[]

    restaurant1 = Restaurant(name='Hilton', address='dedan kimathi street')
    restaurant2 = Restaurant(name='Serena', address='Old Mombasa Road')

    restaurants.append(restaurant1)
    restaurants.append(restaurant2)

    db.session.add_all([restaurant1, restaurant2])
    db.session.commit()

    rp=[]

    restaurant1_pizza1 = RestaurantPizza(price=100, pizza=peperoni, restaurant=restaurant1)
    restaurant1_pizza2 = RestaurantPizza(price=150, pizza=mushroom, restaurant=restaurant1)


    rp.append(restaurant1_pizza1)
    rp.append(restaurant1_pizza2)

    db.session.add_all([restaurant1_pizza1, restaurant1_pizza2])
    db.session.commit()