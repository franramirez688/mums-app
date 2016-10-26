from . import db


def get_menus(purchase):
    pass


def get_products_equal(purchase):
    pass


class PriceType(db.Model):
    """Pricing type depending on the unit used, e.g. kg, gr, ud"""
    __tablename__ = 'price_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    unit = db.Column(db.String(8))
    products = db.relationship("Product",
                               primaryjoin='PriceType.id==Product.price_type_id',
                               backref=db.backref('price_type', lazy='joined'),
                               cascade="all, delete-orphan")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'unit': self.unit,
        }


class ProductType(db.Model):
    """Distinguish between drinks, desserts, main dishes, etc."""
    __tablename__  = 'product_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    products = db.relationship("Product",
                               primaryjoin='ProductType.id==Product.product_type_id',
                               backref=db.backref('product_type', lazy='joined'),
                               cascade="all, delete-orphan")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Product(db.Model):
    """All the products that Mum's web could market"""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    price = db.Column(db.Float(precision=2))
    unit_for_price = db.Column(db.Integer)
    price_type_id = db.Column(db.Integer, db.ForeignKey('price_types.id'))
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_types.id'))

    @property
    def price_type(self):
        return PriceType.query.get(self.price_type_id)

    @property
    def product_type(self):
        return ProductType.query.get(self.product_type_id)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'unit_for_price': self.unit_for_price,
            'price_type': self.price_type.to_json(),
            'product_type': self.product_type.to_json(),
        }

    def apply_offers(self, purchase):
        pass
