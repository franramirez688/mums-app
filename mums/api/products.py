from flask import jsonify, request, current_app, url_for
from . import api
from ..models import Product


@api.route('/products/<int:id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_json())


@api.route('/products/')
def get_user_posts(id):
    pass


@api.route('/products/offer')
def get_user_followed_posts(id):
    pass
