from app.web.blueprint_init import web
from flask import jsonify

@web.route("/user")
def login():
    print("yes")
    return jsonify({"msg":"just a test"})