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
            'products': self.products
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
            'products': self.products
        }

# price_types_data = [
#     {'id': 1, 'name': 'grams', 'unit': 'gr'},
#     {'id': 2, 'name': 'unit', 'unit': 'ud'},
# ]
#
# product_types_data = [
#     {'id': 1, 'name': 'main dish'},
#     {'id': 2, 'name': 'dessert'},
#     {'id': 3, 'name': 'drink'},
# ]


# Productos con un descuento porcentual si se
# compran juntos, por ejemplo el 20% de
# descuento si se compra un menú completo: plato
# principal, bebida y postre.
#
# 2. Descuentos de 3x2. Te llevas 3 unidades del
# mismo producto, y sólo pagas dos.




class Product(db.Model):
    """All the products that Mum's web could market"""
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float(precision=2))
    unit_for_price = db.Column(db.Integer)
    price_type_id = db.Column(db.Integer, db.ForeignKey('price_types.id'))
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_types.id'))


    def to_json(self):
        price_type = PriceType.query.get(self.price_type_id)
        product_type = ProductType.query.get(self.product_type_id)

        json_product = {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'unit_for_price': self.unit_for_price,
            'price_type': price_type.to_json() if price_type is not None else None,
            'product_type': product_type.to_json() if price_type is not None else None,
        }
        return json_product

    def apply_offers(self, purchase):
        pass
