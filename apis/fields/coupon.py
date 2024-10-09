from flask_restx import Namespace, fields


api = Namespace('coupon', description='General coupon')

list_create_coupon_model = api.model('list_create_coupon_model', {
    'id': fields.Integer(readonly=True, description='The unique identifier of the coupon'),
    'discount_type': fields.String(required=True, description='The type of discount (1: percentage, 2: fixed)'),
    'discount': fields.Float(required=True, description='The discount value'),
    'expiration': fields.DateTime(required=True, description='The expiration date of the coupon'),
    'min_purchase': fields.Integer(required=True, description='The minimum purchase required to use the coupon')
})

update_coupon_model = api.model('update_coupon_model', {
    'discount_type': fields.Integer(description='The type of discount (1: percentage, 2: fixed)'),
    'discount': fields.String(description='The discount value'),
    'expiration': fields.DateTime(description='The expiration date of the coupon'),
    'min_purchase': fields.Integer(description='The minimum purchase required to use the coupon')
})

list_coupon_of_user_model = api.model('list_user_coupon_of_user_model', {
    'coupon': fields.Nested(list_create_coupon_model, description='The coupons the user has'),
    'amount': fields.Integer(description='The number of coupons the user has')
})

create_update_coupon_of_user_model = api.model('create_user_coupon_of_user_model', {
    'user_id': fields.Integer(required=True, description='The unique identifier of the user'),
    'coupon_id': fields.Integer(required=True, description='The unique identifier of the coupon'),
    'amount': fields.Integer(default=1, description='The number of coupons the user has')
})