'''
    All the database models
'''

from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class PriceType(Base):
    """Pricing type depending on the unit used, e.g. kg, gr, ud """
    __tablename__ = 'price_type'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    unit = Column(String, nullable=False)

    products = relationship("Product",
                            primaryjoin="PriceType.id==Product.price_type_id",
                            backref=backref("product", cascade="all, delete-orphan"))


class ProductType(Base):
    """Product type, e.g., main dish, dessert """
    __tablename__ = 'product_type'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product",
                            primaryjoin="ProductType.id==Product.product_type_id",
                            backref=backref("product", cascade="all, delete-orphan"))


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    price = Column(Float(precision=2), nullable=False)
    unit_for_price = Column(Integer, nullable=False)
    price_type_id = Column(Integer, ForeignKey('price_type.id'))
    product_type_id = Column(Integer, ForeignKey('product_type.id'))
