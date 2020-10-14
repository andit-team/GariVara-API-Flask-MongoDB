from flask import Response, request, jsonify
from flask_restful import Resource
from extension import mongo
import bson.json_util as bsonO
import datetime
import json
from bson.json_util import dumps


class VehicleTypeList(Resource):
    @staticmethod
    def get() -> Response:
        try:
            dt = mongo.db.vehicleType.find()
            msg = "SUCCESSFUL"
            error = False
        except Exception as ex:
            msg = str(ex)
            error = True
        return jsonify({
            "data": json.loads(dumps(dt)),
            "msg": msg,
            "error": error
        })


class AddVehicleType(Resource):
    @staticmethod
    def post() -> Response:
        data = request.get_json()
        dt = {
            "title": data["title"],
            "create_date": datetime.datetime.now()
        }
        try:
            indexCreate = mongo.db.vehicleType.create_index(
                'title', unique=True)
            ins = mongo.db.vehicleType.insert_one(dt)
            msg = "SUCCESSFUL"
            error = False
        except Exception as ex:
            msg = str(ex)
            error = True
        return jsonify({
            "data": json.loads(dumps(data)),
            "msg": msg,
            "error": error
        })


class EditVehicleType(Resource):
    @staticmethod
    def put() -> Response:
        data = request.get_json()
        try:

            getData = mongo.db.vehicleType.update_one(
                {
                    "_id": bsonO.ObjectId(data["_id"])
                },
                {
                    "$set":
                        {
                            "title": data["title"],
                            "update_date": datetime.datetime.now()
                        }
                })
            msg = "SUCCESSFUL"
            error = False
        except Exception as ex:
            msg = str(ex)
            error = True
        return jsonify({
            "data": json.loads(dumps(data)),
            "msg": msg,
            "error": error
        })


class DeleteVehicleType(Resource):
    @staticmethod
    def put() -> Response:
        data = request.get_json()
        try:

            getData = mongo.db.vehicleType.update_one(
                {
                    "_id": bsonO.ObjectId(data["_id"])
                },
                {
                    "$set":
                        {
                            "title": data["title"],
                            "update_date": datetime.datetime.now()
                        }
                })
            msg = "SUCCESSFUL"
            error = False
        except Exception as ex:
            msg = str(ex)
            error = True
        return jsonify({
            "data": json.loads(dumps(data)),
            "msg": msg,
            "error": error
        })
