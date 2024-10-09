from flask_restx import Resource
from flask import abort

from apis.fields.product import *
from apis.models.product import \
    Product as ProductModel, \
    Category as CategoryModel, \
    Variant as VariantModel
from common.db import db


@api.route('/')
class Products(Resource):
    @api.doc(description='Get all products')
    @api.marshal_with(list_product_model)
    def get(self):
        products = ProductModel.query.all()
        return products
    
    @api.doc(description=\
        """
        Create a product
        Category_id should be leaf nodes (no children).
        """)
    @api.expect(create_product_model)
    @api.marshal_with(list_product_model)
    def post(self):
        data = api.payload
        try:
            # Check category_id
            category = CategoryModel.query.get(data['category_id'])
            if category:
                if category.children:
                    abort(400, description='Attribute category_id should be a leaf node')
            else:
                abort(400, description='Category not found')
            
            # Create product
            if 'variants' in data:
                variants = data.pop('variants')
            product = ProductModel(**data)
            db.session.add(product)
            db.session.flush()
            
            # Create variants
            for var in variants:
                var['product_id'] = product.id
                variant = VariantModel(**var)
                db.session.add(variant)
            
            db.session.commit()  
            return product
        
        except Exception as e:
            import traceback
            traceback.print_exc()
            db.session.rollback()
            abort(400, description=str(e))

@api.route('/variant')
class Variants(Resource):
    @api.doc('Create a variant of product')
    @api.expect(create_variant_of_product_model)
    @api.marshal_with(list_variant_model)
    def post(self):
        data = api.payload
        try:
            variant = VariantModel(**data)
            db.session.add(variant)
            db.session.commit()
        except Exception as e:
            abort(400, description=str(e))
        
@api.route('/category')
class Categories(Resource):
    @api.doc(description='Get all categories')
    @api.marshal_with(list_category_model)
    def get(self):
        categories = CategoryModel.query.filter(CategoryModel.parent_id == None).all()
        return categories