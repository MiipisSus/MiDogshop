from enum import Enum

from common.db import db, BaseModel

class DiscountType(Enum):
    PERCENTAGE = 1
    FIXED_AMOUNT = 2
    
class Coupon(BaseModel):
    __tablename__ = 'coupon'
    
    id = db.Column(db.Integer, primary_key=True)
    discount_type = db.Column(db.Enum(DiscountType), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    expiration = db.Column(db.DateTime, nullable=True)
    min_purchase = db.Column(db.Integer, nullable=True)
    
    users = db.relationship('User_Coupon', back_populates='coupon', lazy=True)
    
class User_Coupon(BaseModel):
    __tablename__ = 'user_coupon'
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, primary_key=True)
    user = db.relationship('User', back_populates='coupons')
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupon.id'), nullable=False, primary_key=True)
    coupon = db.relationship('Coupon', back_populates='users')
    amount = db.Column(db.Integer, nullable=False, default=1)