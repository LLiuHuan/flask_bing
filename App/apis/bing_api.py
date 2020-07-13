from flask import request
from flask_restful import Resource, abort, fields, marshal, marshal_with

from App.models.blue_model import Bing

bing_fields = {
    "copyright": fields.String,
    "imgName": fields.String
}

single_bing_fields = {
    "data": fields.Nested(bing_fields),
    "msg": fields.String,
    "code": fields.Integer,
    "page": fields.Integer,
    "pages": fields.Integer,
    "total": fields.Integer
}

class TabrResource(Resource):
    def options(self):
        print(1234)
        return {'Allow': '*'}, 200, {'Access-Control-Allow-Origin': '*',
                                     'Access-Control-Allow-Methods': 'HEAD, OPTIONS, GET, POST, DELETE, PUT',
                                     'Access-Control-Allow-Headers': 'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild',
                                     }

class BingResource(TabrResource):
    @marshal_with(single_bing_fields)
    def get(self):
        page = int(request.args.get('page')) or 1
        limit = int(request.args.get('limit')) or 9
        if limit > 24:
            limit = 24
        bing_obj = Bing.query.paginate(page=page, per_page=limit)

        return {
            "code": 200,
            "msg": "Get Success",
            "data": bing_obj.items,
            "page": bing_obj.page,
            "pages": bing_obj.pages,
            "total": bing_obj.total
        }

    # 二选一 要么装饰器 要么返回的时候使用marshal
    def post(self):
        page = int(request.args.get('page')) or 1
        limit = int(request.args.get('limit')) or 9
        if int(limit) > 24:
            limit = 24
        bing_obj = Bing.query.paginate(page=page, per_page=limit)
        return_fields = {
            "code": 200,
            "msg": "Post Success",
            "data": bing_obj.items,
            "page": bing_obj.page,
            "pages": bing_obj.pages,
            "total": bing_obj.total
        }

        return marshal(return_fields, single_bing_fields)
