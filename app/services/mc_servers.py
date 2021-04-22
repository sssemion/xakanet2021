from flask_login import current_user

from app.data.db_session import create_session
from app.data.models import MCServer, User
from app.exceptions import ServerAlreadyAdded, ServerConnectionError, ResourceNotFound
from app.services.minecraft import check_connection


def create_server(name, host, rcon_port, rcon_password, nickname, make_active=True):
    with create_session() as session:
        user = session.query(User).get(current_user.id)
        for server in user.mc_servers:
            if server.host == host and server.rcon_port == rcon_port:
                raise ServerAlreadyAdded
        if not check_connection(host, rcon_port, rcon_password):
            raise ServerConnectionError
        server = MCServer(name=name, host=host, rcon_port=rcon_port,
                          rcon_password=rcon_password, nickname=nickname)
        user.mc_servers.append(server)
        session.commit()
        if make_active:
            user.active_mc_server = server.id


def delete_server(server_id):
    with create_session() as session:
        server = session.query(MCServer).get(server_id)
        if server is None:
            raise ResourceNotFound
        if current_user != server.owner:
            raise ResourceNotFound
        if server.owner.active_mc_server == server.id:
            server.owner.active_mc_server = None
        server.owner.mc_servers.remove(server)
        session.delete(server)
