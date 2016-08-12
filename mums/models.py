from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.sql.sqltypes import Integer, String, Float
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class PriceType(Base):
    """Pricing type depending on the unit used, e.g. kg, gr, ud """
    __tablename__ = 'price_type'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    unit = Column(String())

    products = relationship("Product", back_populates="price_type")


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float(precision=2))
    unit_for_price = Column(Integer)
    price_type_id = Column(Integer, ForeignKey('price_type.id'))

    # Relationships to the different prices which could have any product
    price_type = relationship("PriceType", uselist=False, back_populates="product")


class MainDish(Base, Product):
    __tablename__ = 'main_dish'


class Dessert(Base, Product):
    __tablename__ = 'dessert'


class Drink(Base, Product):
    __tablename__ = 'drink'
