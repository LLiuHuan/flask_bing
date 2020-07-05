from flask import request
from flask_restful import Resource, abort, fields, marshal, marshal_with

from App.models.blue_model import Bing

bing_fields = {
    "copyright": fields.String,
    "imgUrl": fields.String
}

single_bing_fields = {
    "data": fields.Nested(bing_fields),
    "msg": fields.String,
    "code": fields.Integer
}

class BingResource(Resource):
    @marshal_with(single_bing_fields)
    def get(self):
        page = int(request.args.get('page')) or 1
        limit = int(request.args.get('limit')) or 9
        if limit > 24:
            limit = 24
        bing_obj = Bing.query.paginate(page=page, per_page=limit)

        return_fields = {
            "code": 200,
            "msg": "Get Success",
            "data": bing_obj.items
        }
        return return_fields

    # 二选一 要么装饰器 要么返回的时候使用marshal
    def post(self):
        page = int(request.args.get('page')) or 1
        limit = int(request.args.get('limit')) or 9
        if int(limit) > 24:
            limit = 24
        bing_obj = Bing.query.paginate(page=page, per_page=limit)
        return_fields = {
            "code": 200,
            "msg": "Get Success",
            "data": bing_obj.items
        }
        return marshal(return_fields, single_bing_fields)
