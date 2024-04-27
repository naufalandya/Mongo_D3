from users import Users

from flask import Blueprint, jsonify
from users import Users

controller_bp = Blueprint('controller', __name__)

@controller_bp.route('/get-users-by-country', methods=['GET'])
def get_users_by_country():
    data = Users.aggregated_users_by_country()

    response = {
        "status": True,
        "message": "ok",
        "data": data
    }

    return jsonify(response)


@controller_bp.route('/get-users-by-age', methods=['GET'])
def get_users_by_age():
    data = Users.aggregated_users_by_age()

    response = {
        "status": True,
        "message": "ok",
        "data": data
    }

    return jsonify(response)
