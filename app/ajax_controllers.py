from flask import Blueprint, jsonify

ajax = Blueprint("ajax", __name__)


@ajax.route("/server/delete/<int:server_id>")
def delete_server(server_id):
    return jsonify({"success": True})

