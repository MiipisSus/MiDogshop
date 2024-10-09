from enum import Enum

from common.db import db, BaseModel


class Product(BaseModel):
    __tablename__ = 'product'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', lazy=True)
    
    variants = db.relationship('Variant', back_populates='product', lazy=True, cascade='all, delete-orphan')
    
class Variant(BaseModel):
    __tablename__ = 'variant'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    image = db.Column(db.String(200), nullable=True)
    
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product', back_populates='variants', lazy=True)
    
class Category(BaseModel):
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    
    children = db.relationship('Category', backref=db.backref('parent', remote_side=[id]), lazy=True)