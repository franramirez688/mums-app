from . import db


class PriceType(db.Model):
    """Pricing type depending on the unit used, e.g. kg, gr, ud """
    __tablename__ = 'price_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    unit = db.Column(db.String(8))

    products = db.relationship("Product",
                               backref=db.backref('price_type', lazy='joined'),
                               cascade="all, delete-orphan")


class ProductType(db.Model):

    __tablename__  = 'product_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))

    products = db.relationship("Product",
                               backref=db.backref('product_type', lazy='joined'),
                               cascade="all, delete-orphan")


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float(precision=2))
    unit_for_price = db.Column(db.Integer)
    price_type_id = db.Column(db.Integer, db.ForeignKey('price_types.id'))
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_types.id'))
