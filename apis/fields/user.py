from flask_restx import Namespace, fields

from apis.fields.coupon import list_coupon_of_user_model

api = Namespace('user', description='General users')

create_list_address_model = api.model('create_list_address_model', {
    'id': fields.Integer(readonly=True, description='The address id'),
    'country_code': fields.String(required=True, description='The address country_code'),
    'state_province_county': fields.String(description='The address state_province_county'),
    'city': fields.String(required=True, description='The address city'),
    'address_line_1': fields.String(required=True, description='The address line 1'),
    'address_line_2': fields.String(description='The address line 2'),
    'address_line_3': fields.String(description='The address line 3'),
    'postcode': fields.String(required=True, description='The address postcode'),
    'other_address_details': fields.String(description='The address other_address_details')
})

update_address_model = api.model('update_address_model', {
    'country_code': fields.String(description='The address country_code'),
    'state_province_county': fields.String(description='The address state_province_county'),
    'city': fields.String(description='The address city'),
    'address_line_1': fields.String(description='The address line 1'),
    'address_line_2': fields.String(description='The address line 2'),
    'address_line_3': fields.String(description='The address line 3'),
    'postcode': fields.String(description='The address postcode'),
    'other_address_details': fields.String(description='The address other_address_details')
})

list_user_model = api.model('list_user_model', {
    'id': fields.Integer(readonly=True, description='The user id'),
    'username': fields.String(required=True, description='The user name'),
    'email': fields.String(required=True, description='The user email'),
    'home_phone_number': fields.String(required=True, description='The user home phone number'),
    'mobile_phone_number': fields.String(required=True, description='The user mobile phone number'),
    'address': fields.Nested(create_list_address_model, description='The user address'),
    'coupons': fields.Nested(list_coupon_of_user_model, description='The coupons of the user')
})

create_user_model = api.model('create_user_model', {
    'username': fields.String(required=True, description='The user name'),
    'password_hash': fields.String(required=True, description='The user password'),
    'email': fields.String(required=True, description='The user email'),
    'home_phone_number': fields.String(required=True, description='The user home phone number'),
    'mobile_phone_number': fields.String(required=True, description='The user mobile phone number'),
    'address': fields.Nested(create_list_address_model, description='The user address')
})

update_user_model = api.model('update_user_model', {
    'username': fields.String(description='The user name'),
    'password_hash': fields.String(description='The user password'),
    'email': fields.String(description='The user email'),
    'home_phone_number': fields.String(description='The user home phone number'),
    'mobile_phone_number': fields.String(description='The user mobile phone number'),
    'address': fields.Nested(update_address_model, description='The user address')
})

