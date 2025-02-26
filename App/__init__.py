from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import envs
from App.views import init_blue
from flask_cors import *

def create_app(env):
    app = Flask(__name__)

    CORS(app)

    # 初始化配置
    app.config.from_object(envs.get(env))

    # 初始化路由
    init_blue(app)

    # 初始化第三方应用
    init_ext(app)

    # 初始化RESTFul
    init_api(app)

    return app
