from . import db


class PriceType(db.Model):
    """Pricing type depending on the unit used, e.g. kg, gr, ud """
    __tablename__ = 'price_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    unit = db.Column(db.String())

    products = db.relationship("Product", backref="price_type")


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float(precision=2))
    unit_for_price = db.Column(db.Integer)
    price_type_id = db.Column(db.Integer, db.ForeignKey('price_type.id'))

    # Relationships to the different prices which could have any product
    price_type = db.relationship("PriceType", backref="product")


class MainDish(Product):
    __tablename__ = 'main_dish'


class Dessert(Product):
    __tablename__ = 'dessert'


class Drink(Product):
    __tablename__ = 'drink'
