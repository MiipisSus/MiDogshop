from flask_sqlalchemy import SQLAlchemy

from common.db import db
from app import app


with app.app_context():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()
