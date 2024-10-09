from flask_restx import Namespace, fields
from apis.models.product import Product

api = Namespace('product', description='General products')

list_variant_model = api.model('list_variant_model', {
    'id': fields.Integer(description='The unique identifier of the variant'),
    'name': fields.String(description='The name of the variant'),
    'price': fields.Float(description='The price of the variant'),
    'stock': fields.Integer(description='The stock of the variant', default=0),
    'image': fields.String(description='The image URL of the variant'),
})

create_variant_of_product_model = api.model('create_variant_of_product_model', {
    'name': fields.String(required=True, description='The name of the variant'),
    'price': fields.Float(required=True, description='The price of the variant'),
    'stock': fields.Integer(required=True, description='The stock of the variant', default=0),
    'image': fields.String(description='The image URL of the variant'),
})

create_variant_model = api.model('create_variant_model', {
    'name': fields.String(required=True, description='The name of the variant'),
    'price': fields.Float(required=True, description='The price of the variant'),
    'stock': fields.Integer(required=True, description='The stock of the variant', default=0),
    'image': fields.String(description='The image URL of the variant'),
    'product_id': fields.Integer(required=True, description='The unique identifier of the category')
})

list_category_of_product_model = api.model('list_category_model', {
    'id': fields.Integer(required=True, description='The unique identifier of the category'),
    'name': fields.String(required=True, description='The name of the category')
})

list_category_model = api.model('list_category_model', model=list_category_of_product_model)

list_category_of_product_model['parent'] = fields.List(fields.Nested(list_category_of_product_model), description='List of parent categories', nullable=True)
list_category_model['children'] = fields.List(fields.Nested(list_category_model), description='List of child categories', nullable=True)

list_product_model = api.model('list_product_model', {
    'id': fields.Integer(readonly=True, description='The unique identifier of the product'),
    'name': fields.String(description='The name of the product'),
    'description': fields.String(description='A detailed description of the product'),
    'category': fields.Nested(list_category_of_product_model, description='The category to which the product belongs'),
    'variants': fields.Nested(list_variant_model, description='List of variants associated with the product, such as different sizes or colors')
})

create_product_model = api.model('create_product_model', {
    'name': fields.String(required=True, description='The name of the product'),
    'description': fields.String(required=True, description='A detailed description of the product'),
    'category_id': fields.Integer(required=True, description='The category to which the product belongs'),
    'variants': fields.List(fields.Nested(create_variant_of_product_model, description='List of variants associated with the product, such as different sizes or colors'))
})
