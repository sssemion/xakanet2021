from flask import Blueprint, jsonify

from app.exceptions import ResourceNotFound
from app.services.mc_servers import delete_server

ajax = Blueprint("ajax", __name__)


@ajax.route("/server/delete/<int:server_id>", methods=["POST"])
def delete_server_controller(server_id):
    try:
        delete_server(server_id)
        return jsonify({"success": True})
    except ResourceNotFound as e:
        return jsonify({"success": False, "message": str(e)})
