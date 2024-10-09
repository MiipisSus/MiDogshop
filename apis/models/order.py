from enum import Enum

from common.db import db, BaseModel
    
    
class DeliveryType(Enum):
    HOME = 0
    SEVEN_ELEVEN = 1
    FAMILYMART = 2

class PaymentMethod(Enum):
    CASH_ON_DELIVERY = 0
    CREDIT_CARD = 1

class Order(BaseModel):
    __tablename__ = 'order'
    
    id = db.Column(db.Integer, primary_key=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='orders', lazy=True)
    
    coupon_id = db.Column(db.Integer, db.ForeignKey('coupon.id'), nullable=True)
    coupon = db.relationship('Coupon', lazy=True)
    
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'))
    delivery = db.relationship('Delivery', lazy=True)
    
    payment_method = db.Column(db.Enum(PaymentMethod), nullable=False)
    creditcard_id = db.Column(db.Integer, db.ForeignKey('creditcard.id'), nullable=True)
    creditcard = db.relationship('Creditcard', lazy=True)
    
class Delivery(BaseModel):
    __tablename__ = 'delivery'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    delivery_type = db.Column(db.Enum(DeliveryType), nullable=False)
    
    # For CVS code
    store_code = db.Column(db.String, nullable=True)
    
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship('Address', lazy=True)
    
    user = db.relationship('User', back_populates='deliveries', lazy=True)
    
class Creditcard(BaseModel):
    __tablename__ = 'creditcard'
    
    id = db.Column(db.Integer, primary_key=True)
    cardholder_name = db.Column(db.String(100), nullable=False)
    last_four_digits = db.Column(db.String(4), nullable=False)
    expiration_year = db.Column(db.Integer, nullable=False)
    expiration_month = db.Column(db.Integer, nullable=False)
    card_type = db.Column(db.String(20), nullable=False)
    issuing_bank = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    most_used = db.Column(db.Boolean, default=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='creditcards', lazy=True)
    