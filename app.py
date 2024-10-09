from flask import Flask

from apis import blueprint as api_blueprint
from config import Config
from common.db import db
from common.migrate import migrate

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

from apis.models import user, product, coupon, order

app.register_blueprint(api_blueprint, prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)