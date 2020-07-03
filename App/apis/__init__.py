from flask_restful import Api

from App.apis.bing_api import BingResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(BingResource, "/img/bing/")
