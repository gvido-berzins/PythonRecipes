from . import db, create_app, models


def init_db(app=create_app()):
    db.create_all(app=app)


