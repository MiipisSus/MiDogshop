from common.db import db
from app import app
from apis.models.product import Product, Variant

product_dict = {
    'Airpod 盤子限量版': 4,
    '彩虹牌喇叭': 5,
    'Razer 無線電競滑鼠': 7,
    '夢幻牌雙門冰箱': 11,
    '兇兇肥婆洗衣機': 12,
    '自定義 唱歌掃地機器人 周杰倫限量版': 15,
    '敷了一定白泡泡 面膜': 18,
    '欸死K兔 貴到你破產化妝水': 19,
    '植村秀 跟植物一樣自然粉底液': 21,
    '妹比林 便宜又好用遮暇霜': 22,
    '長生不老藥': 24,
    '蓮花朵朵開餅乾': 28,
    '小胸友善 A變E超級內衣': 32,
    '洗完變希臘女神 神話洗髮精': 48,
    '會被偷零件 小蜜蜂擋車': 80
}

def create_product():
    for product, cat_id in product_dict.items():
        data = {
            'name': product,
            'description': 'Mia mia mia',
            'category_id': cat_id
        }
        product = Product(**data)
        db.session.add(product)
    
    db.session.commit()

def create_variant():
    data = {
        'name': '白色',
        'price': 4500,
        'stock': 10,
        'product_id': 1
    }
    variant = Variant(**data)
    db.session.add(variant)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        # create_product()
        create_variant()