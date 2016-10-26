from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Product


@api.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_json())


@api.route('/products/', methods=['GET'])
def get_all_products():
    ret = []
    products = Product.query.all()
    for product in products:
        ret.append(product.to_json())
    return jsonify(ret)


@api.route('/products/offer', methods=['GET'])
def get_offer(id):
    pass
