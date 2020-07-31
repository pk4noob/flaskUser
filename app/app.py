from app_init.app_factory import createAp
from flask import jsonify, current_app, request
from http import HTTPStatus
import os
import warnings
from flask import Flask, request, jsonify, send_file, send_from_directory
from app.seralize import UserSchema
from app.model import User
from http import HTTPStatus
from marshmallow import ValidationError
from pprint import pprint

warnings.simplefilter("ignore")
settings_name = os.getenv("settings")
app = createAp(settings_name)


@app.route("/user", methods=["POST"])
def createPost():
    data = request.get_json()
    try:
        x = UserSchema().load(data)
        x.pasword_hash()
        x.savedb()
    except ValidationError as err:
        return jsonify(err.messages), HTTPStatus.BAD_REQUEST
    return UserSchema().jsonify(x), HTTPStatus.OK


@app.route("/user/<int:id>", methods=["GET"])
def createget(id):
    dataa = User.query.filter_by(id=id).first()
    if dataa:
        return UserSchema().jsonify(dataa), HTTPStatus.OK
    return jsonify(msg="Error"), HTTPStatus.NOT_FOUND


@app.route("/user", methods=["GET"])
def createAll():
    dataAll = User.query.all()
    return UserSchema().jsonify(dataAll, many=True), HTTPStatus.OK


@app.route("/user/<int:id>", methods=["PUT"])
def updateMethods(id):
    dataupdate = User.query.filter_by(id=id).first()
    if dataupdate:
        dataa = request.get_json()
        dataupdate.update(**dataa)
        return UserSchema().jsonify(dataa), HTTPStatus.OK
    return jsonify(msg="error"), HTTPStatus.BAD_REQUEST


@app.route("/user/<int:id>", methods=["DELETE"])
def deleteMethods(id):
    delet = User.query.filter_by(id=id).first()
    if delet:
        delet.deletedb()
        return jsonify(messege="silindi"), HTTPStatus.OK
    return jsonify(messege="silindiii"), HTTPStatus.bad
