from flask_restx import Resource
from flask import abort
from datetime import datetime

from apis.fields.coupon import *
from apis.models.coupon import \
    Coupon as CouponModel, \
    User_Coupon as User_CouponModel, \
    DiscountType
from common.db import db

@api.route('/')
class Coupons(Resource):
    @api.doc(description='Get all coupons')
    @api.marshal_with(list_create_coupon_model)
    def get(self):
        coupons = CouponModel.query.all()
        return coupons
    
    @api.doc(description=\
            """
            Create a coupon
            
            discount_type enum:
            0 -> PERCENTAGE
            1 -> FIXED_AMOUNT
            
            expiration format:
            'YYYY-MM-DD'
            """)
    @api.expect(list_create_coupon_model)
    @api.marshal_with(list_create_coupon_model)
    def post(self):
        data = api.payload
        try:
            data['discount_type'] = DiscountType(data['discount_type'])
            data['expiration'] = datetime.strptime(data['expiration'], '%Y-%m-%d')
            coupon = CouponModel(**data)
            db.session.add(coupon)
            db.session.commit()
            
            return coupon
        
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))

@api.route('/to_user')
class User_Coupons(Resource):
    @api.doc(description=\
            """
            Create a coupon avaliable to a user
            If the user already possesses this coupon, the amount will be increased. 
            """)
    @api.expect(create_update_coupon_of_user_model)
    @api.marshal_with(create_update_coupon_of_user_model)
    def post(self):
        data = api.payload
        try:
            user_coupon = User_CouponModel.query.filter(User_CouponModel.user_id == data['user_id'],
                                                         User_CouponModel.coupon_id == data['coupon_id']).first()
            if user_coupon:
                user_coupon.amount += data['amount']
            else:
                user_coupon = User_CouponModel(**data)
                db.session.add(user_coupon)
    
            db.session.commit()
            return user_coupon
        except Exception as e:
            abort(400, description=str(e))