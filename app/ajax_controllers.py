from flask import Blueprint, jsonify

from app.controllers import only_for_authenticated_and_confirmed
from app.exceptions import ResourceNotFound, NotEnoughMoney, RconCommandError
from app.services.mc_servers import delete_server
from app.services.users import give_item_handler, set_active_server, act_creeper_handler, act_web_handler, \
    act_sand_handler

ajax = Blueprint("ajax", __name__)


@ajax.route("/server/delete/<int:server_id>", methods=["POST"])
@only_for_authenticated_and_confirmed
def delete_server_controller(server_id):
    try:
        delete_server(server_id)
        return jsonify({"success": True})
    except ResourceNotFound as e:
        return jsonify({"success": False, "message": str(e)}), 400


@ajax.route("/server/activate/<int:server_id>", methods=["POST"])
@only_for_authenticated_and_confirmed
def activate_server(server_id):
    try:
        set_active_server(server_id)
    except ResourceNotFound as e:
        return jsonify({"success": False, "message": str(e)}), 400
    return jsonify({"success": True})


@ajax.route("/user/<username>/give/<int:item_id>", methods=["POST"])
@only_for_authenticated_and_confirmed
def give_item_controller(username, item_id):
    try:
        give_item_handler(username, item_id)
        return jsonify({"success": True})
    except (ResourceNotFound, NotEnoughMoney, RconCommandError) as e:
        return jsonify({"success": False, "message": str(e)}), 400


@ajax.route("/user/<username>/act/creeper", methods=["POST"])
@only_for_authenticated_and_confirmed
def act_creeper_controller(username):
    try:
        act_creeper_handler(username)
        return jsonify({"success": True})
    except (ResourceNotFound, NotEnoughMoney, RconCommandError) as e:
        return jsonify({"success": False, "message": str(e)}), 400


@ajax.route("/user/<username>/act/web", methods=["POST"])
@only_for_authenticated_and_confirmed
def act_web_controller(username):
    try:
        act_web_handler(username)
        return jsonify({"success": True})
    except (ResourceNotFound, NotEnoughMoney, RconCommandError) as e:
        return jsonify({"success": False, "message": str(e)}), 400


@ajax.route("/user/<username>/act/sand", methods=["POST"])
@only_for_authenticated_and_confirmed
def act_sand_controller(username):
    try:
        act_sand_handler(username)
        return jsonify({"success": True})
    except (ResourceNotFound, NotEnoughMoney, RconCommandError) as e:
        return jsonify({"success": False, "message": str(e)}), 400
