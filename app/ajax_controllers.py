from flask import Blueprint, jsonify

ajax = Blueprint("ajax", __name__)


@ajax.route("/server/delete/<int:server_id>", methods=["POST"])
def delete_server(server_id):
    return jsonify({"success": True})


@ajax.route("/server/activate/<int:server_id>", methods=["POST"])
def activate_server(server_id):
    return jsonify({"success": True})
