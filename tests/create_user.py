import random, string
import traceback
import requests
from faker import Faker

from common.db import db
from common.utils import hash_password
from apis.models.user import User, Address
from app import app

faker = Faker()

def create_random_user():
    address = create_random_address()
    data = {
        'username': faker.user_name(),
        'password_hash': hash_password(faker.password(length=10)),
        'email': faker.email(),
        'home_phone_number': faker.phone_number(),
        'mobile_phone_number': faker.phone_number(),
        'address_id': address.id
    }
    try:
        user = User(**data)
        db.session.add(user)
        db.session.commit()
    except:
        print(traceback.print_exc())

def create_random_address():
    data = {
    'country_code': faker.country_code(),
    'city': faker.city(),
    'address_line_1': faker.street_address(),
    'postcode': faker.postcode()
    }
    address = Address(**data)
    try:
        db.session.add(address)
        db.session.commit()
        
        return address
    except:
        print(traceback.print_exc())

def post_user():
    data = {
        'username': faker.user_name(),
        'password_hash': hash_password(faker.password(length=10)),
        'email': faker.email(),
        'home_phone_number': faker.phone_number(),
        'mobile_phone_number': faker.phone_number(),
        'address': {
            'country_code': faker.country_code(),
            'city': faker.city(),
            'address_line_1': faker.street_address(),
            'postcode': faker.postcode()
        }
    }
    
    res = requests.post('http://127.0.0.1:5000/user/', json=data)
    print(res, res.text)

def patch_user():
    data = {
        'username': faker.user_name(),
        'address': {
            'country_code': faker.country_code(),
            'city': faker.city(),
            'address_line_1': faker.street_address(),
            'postcode': faker.postcode()
        }
    }
    res = requests.patch('http://127.0.0.1:5000/user/52', json=data)
    print(res, res.text)

def test():
    data = {
        "id": 52,
        "username": "cherylmitchell",
        "email": "ronald44@example.com",
        "home_phone_number": "001-422-613-6320x3758",
        "mobile_phone_number": "001-833-492-2302",
        "address": {
            "id": None,
            "country_code": None,
            "state_province_county": None,
            "city": None,
            "address_line_1": None,
            "address_line_2": None,
            "address_line_3": None,
            "postcode": None,
            "other_address_details": None
    }
}
    address = Address.query.get(data['address']['id'])
    print(address)
    
def ran_str(length: list, string_type: int=2):
    '''
    length: [start, end]
    
    string_type:
    
    0 -> integer only
    
    1 -> string only
    
    2 -> mix
    
    '''
    length = random.randint(length[0], length[1])
        
    if string_type == 0:
        letters = string.digits
    elif string_type == 1:
        letters = string.ascii_letters
    else:
        letters = string.digits + string.ascii_letters
        
    random_string = ''.join(random.choice(letters) for _ in range(length))
    
    return random_string


if __name__ == '__main__':
    with app.app_context():
        # create_random_user()
        patch_user()