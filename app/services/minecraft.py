from mcrcon import MCRcon


def give_effect(player, effect, duration, s, address, port, password):
    with MCRcon(address, password, port=port) as mcr:
        mcr.command("effect give" + player + " " + effect + str(duration) + " " + str(s))


def give_item(player, item, count, address, port, password):
    with MCRcon(address, password, port=port) as mcr:
        mcr.command(f"give {player} {item} {count}")


def ench_item(player, ench, count, address, port, password):
    with MCRcon(address, password, port=port) as mcr:
        mcr.command(f"enchant {player} {ench} {count}")


def best_time(address, port, password):
    with MCRcon(address, password, port=port) as mcr:
        mcr.command("time set day")
        mcr.command("weather clear")


def check_connection(address, port, password):
    try:
        with MCRcon(address, password, port=port):
            return True
    except ConnectionRefusedError:
        return False


def start_mini_game(pl1, pl2, address, port, password):
    with MCRcon(address, password, port=port) as mcr:
        mcr.command("fill 10 254 10 30 255 30 minecraft:bedrock")
        mcr.command(f"tp {pl1} 10 257 10")
        mcr.command(f"tp {pl2} 30 257 30")
        mcr.command("clear" + " " + pl1)
        mcr.command("clear" + " " + pl2)
        mcr.command("effect give " + pl1 + " speed 100 10")
        mcr.command("effect give " + pl1 + " regeneration 100 100")
        mcr.command("effect give " + pl2 + " regeneration 100 100")
        mcr.command("effect give " + pl2 + " speed 100 10")
        mcr.command(f"give {pl1} " + "stick{Enchantments:[{id:knockback,lvl:3}, {id:channeling,lvl:1}]} 1")
        mcr.command(f"give {pl2} " + "stick{Enchantments:[{id:knockback,lvl:3}]} 1")
