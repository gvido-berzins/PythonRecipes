from . import create_app, db, models


def init_db(app=create_app()):
    db.create_all(app=app)
