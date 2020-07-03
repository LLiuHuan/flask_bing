from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # 操作数据库
migrate = Migrate()  # 数据库迁移


def init_ext(app):
    db.init_app(app)  # 使用app初始化SQLAlchemy
    migrate.init_app(app, db)  # 使用app初始化Migrate
    Session(app)
    DebugToolbarExtension(app)