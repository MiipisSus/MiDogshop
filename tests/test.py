import random
from datetime import datetime, timedelta

from app import app
from apis.models.product import Product

def create_coupon():
    # 取得當前時間
    now = datetime.now()

    # 設置未來1年的時間範圍（365天）
    future_time = timedelta(days=365)

    # 確保隨機秒數在合理範圍內，避免溢出
    random_seconds = random.randint(0, int(future_time.total_seconds()))

    # 計算未來隨機日期時間
    try:
        random_future_date = now + timedelta(seconds=random_seconds)
        print(random_future_date)
    except OverflowError as e:
        print(f"Error: {e}")

# 調用函數
# create_coupon()

with app.app_context():
    print(Product.__dict__)