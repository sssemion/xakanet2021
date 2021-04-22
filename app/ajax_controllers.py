from flask import Blueprint, jsonify

from app.controllers import only_for_authenticated_and_confirmed
from app.exceptions import ResourceNotFound
from app.services.mc_servers import delete_server
from app.services.users import give_item_handler

ajax = Blueprint("ajax", __name__)


@ajax.route("/server/delete/<int:server_id>", methods=["POST"])
@only_for_authenticated_and_confirmed
def delete_server_controller(server_id):
    try:
        delete_server(server_id)
        return jsonify({"success": True})
    except ResourceNotFound as e:
        return jsonify({"success": False, "message": str(e)})


@ajax.route("/user/<username>/give/<int:item_id>", methods=["POST"])
@only_for_authenticated_and_confirmed
def give_item_controller(username, item_id):
    try:
        give_item_handler(username, item_id)
        return jsonify({"success": True})
    except ResourceNotFound as e:
        return jsonify({"success": False, "message": str(e)})
