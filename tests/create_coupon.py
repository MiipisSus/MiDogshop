import random
from datetime import timedelta, datetime

from common.db import db
from apis.models.coupon import Coupon, User_Coupon, DiscountType
from apis.models.user import User
from app import app

def create_coupon():  
    for _ in range(10):
        random_secs = random.randint(0, int(timedelta(days=365).total_seconds()))
        random_date = datetime.now() + timedelta(seconds=random_secs)
        discount_type = random.randint(1, 2)
        if discount_type == 1:
            discount = random.randint(10, 19) * 0.05
        else:
            discount = random.randrange(10, 200, 50)
        
        data = {
            'discount_type':  DiscountType(discount_type),
            'discount': discount,
            'expiration': random_date,
            'min_purchase': random.randrange(0, 500, 50)
        }
        coupon = Coupon(**data)
        db.session.add(coupon)
    
    db.session.commit()    

def create_user_coupons():
    data = {
        'user_id': 1,
        'coupon_id': 1,
        'amount': 1
    }
    user_coupon = User_Coupon.query.filter(User_Coupon.user_id == data['user_id'],
                                           User_Coupon.coupon_id == data['coupon_id']).first()
    if user_coupon:
        user_coupon.amount += data['amount']
    else:
        user_coupon = User_Coupon(**data)
        db.session.add(user_coupon)
    
    db.session.commit()
    
if __name__ == '__main__':
    with app.app_context():
        # create_coupon()
        create_user_coupons()