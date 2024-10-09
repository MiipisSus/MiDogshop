from flask_restx import Resource
from flask import abort

from apis.fields.user import *
from apis.models.user import \
    User as UserModel, Address as AddressModel
from common.db import db
from common.utils import hash_password


@api.route('/')
class Users(Resource):
    @api.doc(description='Get all users')
    @api.response(200, 'User successfuly return user infomation')
    @api.marshal_list_with(list_user_model)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @api.doc(description='Create a user')
    @api.response(201, 'User successfully created')
    @api.response(400, 'Validation Error')
    @api.expect(create_user_model, validate=True)
    @api.marshal_with(list_user_model, code=201)
    def post(self):
        data = api.payload
        
        try:
            # Address
            if 'address' in data:
                    new_address = AddressModel(**data['address'])
                    db.session.add(new_address)
                    db.session.flush()

                    data.pop('address')
                    data['address_id'] = new_address.id        
            # User
            new_user = UserModel(**data)
            new_user.password_hash = hash_password(new_user.password_hash)

            db.session.add(new_user)
            db.session.commit()
            return new_user, 201
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))
    

@api.route('/<int:id>')
class User(Resource):
    @api.doc(description='Get a user')
    @api.response(200, 'User successfuly return user infomation')
    @api.response(404, 'User not found')
    @api.marshal_with(list_user_model)
    def get(self, id):
        user = UserModel.query.get(id)
        if user is None:
            abort(404, description='User not found')
        
        return user
    
    @api.doc(description='Update a user')
    @api.response(201, 'User successfully updated')
    @api.response(404, 'User not found')
    @api.expect(update_user_model)
    @api.marshal_with(list_user_model)
    def patch(self, id):
        data = api.payload
        
        try:
            # Address
            if 'address' in data:
                address = UserModel.query.get(id).address
                
                if address is None:
                    address = AddressModel(**data['address'])
                    db.session.add(address)
                    db.session.flush()
                    
                for key, value in data['address'].items():
                    if hasattr(address, key):
                        setattr(address, key, value)
                
                data.pop('address')
                data['address_id'] = address.id   
                
            # User
            user = UserModel.query.get(id)
            
            if user is None:
                abort(404, description='User not found')
                
            for key, value in data.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            
            db.session.commit()
                
            return user
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))
            
    @api.doc(description='Delete a user')
    @api.response(201, 'User successfully deleted')
    @api.response(404, 'User not found')
    @api.marshal_with(list_user_model)
    def delete(self, id):
        user = UserModel.query.get(id)
        
        if user is None:
            abort(404, description='User not found')
            
        try:
            db.session.delete(user)
            db.session.commit()

            return user
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))
            
@api.route('/address')
class Addresses(Resource):
    @api.deprecated
    @api.doc('create a address for user')
    @api.response(201, 'Address successfully created')
    @api.response(400, 'Validation Error')
    @api.expect(create_list_address_model)
    @api.marshal_with(create_list_address_model)
    def post(self):
        data = api.payload
        new_address = AddressModel(**data)
        
        try:
            db.session.add(new_address)
            db.session.commit()
            
            return new_address, 201
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))

@api.route('/address/<int:id>')
class Address(Resource):
    @api.deprecated
    @api.doc('update a address for user')
    @api.response(201, 'Address successfully updated')
    @api.response(404, 'Address not found')
    @api.expect(update_address_model)
    @api.marshal_with(update_address_model)
    def patch(self, id):
        data = api.payload
        address = AddressModel.query.get(id)
        
        for key, value in data.items():
            if hasattr(address, key):
                setattr(address, key, value)
        
        try:
            db.session.commit()

            return address
        except Exception as e:
            db.session.rollback()
            abort(400, description=str(e))
            
