from user import user_factory
from flask import Flask, jsonify, request 
from werkzeug.exceptions import HTTPException
import traceback
import json
app = Flask(__name__)


@app.route('/user/<user_id>', methods=["GET","DELETE","PATCH","POST"])
def user(user_id = None):
    try:
        if request.method == "GET":
            res = user_factory.get_user(user_id)
            return res
        elif request.method == "PATCH":
            res = user_factory.update_user(user_id, json.loads(request.data))
        elif request.method == "DELETE":
            res = user_factory.delete_user(user_id)
        return res, 200
    except Exception as e:
        print("Some exception occoured :",traceback.format_exc())


@app.route('/user/', methods=["POST"])
def create_user():
    try:
        res = user_factory.create_user(json.loads(request.data) )
        return res, 200
    except Exception as e:
        print("Some exception occoured :",traceback.format_exc())
        return 500, "An error occoured"

if __name__ == "__main__":
    # app = create_app()
    app.run(debug=True)