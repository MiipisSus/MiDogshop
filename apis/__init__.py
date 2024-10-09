from flask import Blueprint
from flask_restx import Api

from .namespaces.user import api as user_api
from .namespaces.product import api as product_api
from .namespaces.coupon import api as coupon_api


blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='SPMS',
    version='1.0',
    description='Shopping Platform Management System'
)

api.add_namespace(user_api)
api.add_namespace(product_api)
api.add_namespace(coupon_api)