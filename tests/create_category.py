from faker import Faker

from common.db import db
from app import app
from apis.models.product import Category

category_dict = \
    {
        '3C': {
            '數位週邊': {
                '穿戴裝置': None,
                '耳機/藍芽耳機': None,
                '喇叭/藍芽喇叭': None
                },
            '資訊週邊': {
                '滑鼠/鍵盤': None,
                '電腦週邊': None
            }
            },
        '家電': {
            '廚房專區': {
                '冰箱': None,
                '洗衣機': None
                },
            '生活專區': {
                '吸塵器': None,
                '掃地機': None
            }
            },
        '美妝保養': {
            '臉部保養': {
                '面膜': None,
                '化妝水': None
                },
            '彩妝用品': {
                '專櫃彩妝': None,
                '開架彩妝': None
            }
            },
        '保健食品': {
            '養生保健': {
                '維他命': None,
                '葉黃素': None
                },
            '飲料零食': {
                '餅乾': None,
                '飲料': None
            }
            },
        '服飾內衣': {
            '女裝': {
                '女上衣': None,
                '女下著': None,
                },
            '男裝': {
                '男上衣': None,
                '男下著': None,
            }
            },
        '鞋包精品': {
            '女鞋': {
                '女休閒鞋': None,
                '女高跟鞋': None
                },
            '男鞋': {
                '男休閒鞋': None
            }
            },
        '母嬰用品': {
            '兒童用品': {
                '地墊圍欄': None,
                '文具用品': None
                },
            '個人清潔': {
                '洗髮護髮': None,
                '口腔清潔': None
            }
            },
        '圖書文具': {
            '知識理財': {
                '商業理財': None,
                '語言學習': None
                },
            '文教藝術': {
                '辦公用品': None,
                '學習用品': None
            }
            },
        '傢寢運動': {
            '家具': {
                '床架': None,
                '沙發': None
                },
            '收納': {
                '收納櫃': None,
                '收納架': None
                },
            '寢具': {
                '枕頭/枕套': None,
                '床墊': None
            }
            },
        '日用生活': {
            '個人用品': {
                '衛生紙': None,
                '衛生棉': None
                },
            '家居清潔': {
                '清潔精': None,
                '洗衣精/粉': None
                },
            },
        '旅遊戶外': {
            '戶外露營': {
                '露營': None,
                '登山健行': None
                },
            '車類': {
                '自行車': None,
                '機車': None
            }
        }
    }

def init_category():
    for root, sub in category_dict.items():
        # 創建第一層分類
        cat = Category(name=root)
        db.session.add(cat)
        db.session.flush()  # 保證 cat.id 生成

        if sub:
            for sec_sub, third_sub in sub.items():
                # 創建第二層分類
                sec_cat = Category(name=sec_sub, parent_id=cat.id)  # 使用第一層分類的 ID 作為 parent_id
                db.session.add(sec_cat)
                db.session.flush()  # 保證 sec_cat.id 生成

                if third_sub:
                    for fourth_sub, fifth_sub in third_sub.items():
                        # 創建第三層分類
                        third_cat = Category(name=fourth_sub, parent_id=sec_cat.id)  # 使用第二層分類的 ID 作為 parent_id
                        db.session.add(third_cat)
                        db.session.flush()  # 保證 third_cat.id 生成

        db.session.commit()  # 提交一批數據

def show_children():
    cat: Category = db.session.get(Category, 1)
    for cat in cat.children:
        print(cat.__dict__)
    
if __name__ == '__main__':
    with app.app_context():
        show_children()