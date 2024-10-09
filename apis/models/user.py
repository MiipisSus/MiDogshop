from common.db import db, BaseModel


class User(BaseModel):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    home_phone_number = db.Column(db.String(30), unique=True, nullable=False)
    mobile_phone_number = db.Column(db.String(30), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=True)
    address = db.relationship('Address', lazy=True, cascade='all, delete-orphan', single_parent=True)
    
    orders = db.relationship('Order', back_populates='user', lazy=True, cascade='all, delete-orphan')
    
    deliveries = db.relationship('Delivery', back_populates='user', lazy=True, cascade='all, delete-orphan')
    
    coupons = db.relationship('User_Coupon', back_populates='user', lazy=True)
    
    creditcards = db.relationship('Creditcard', back_populates='user', lazy=True, cascade='all, delete-orphan')

class Address(BaseModel):
    __tablename__ = 'address'
    
    id = db.Column(db.Integer, primary_key=True)
    country_code = db.Column(db.String, nullable=False)
    state_province_county = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(100), nullable=False)
    address_line_1 = db.Column(db.String(100), nullable=False)
    address_line_2 = db.Column(db.String(100), nullable=True)
    address_line_3 = db.Column(db.String(100), nullable=True)
    postcode = db.Column(db.String, nullable=False)
    other_address_details = db.Column(db.String(100), nullable=True)