from mcrcon import MCRcon
from random import randint


def give_effect(player, effect, duration, s, adress="46.174.54.100", port=26576,
                password="LojSwh77x25e4c3SXMSUWvz23bWn5tM6"):
    with MCRcon(adress, password, port=port) as mcr:
        mcr.command("effect give" + player + " " + effect + str(duration) + " " + str(s))


def give_item(player, item, count, adress="46.174.54.100", port=26576, password="LojSwh77x25e4c3SXMSUWvz23bWn5tM6"):
    with MCRcon(adress, password, port=port) as mcr:
        c = mcr.command(f"give {player} {item} {count}")
        print(c)


def ench_item(player, ench, count, adress="46.174.54.100", port=26576, password="LojSwh77x25e4c3SXMSUWvz23bWn5tM6"):
    with MCRcon(adress, password, port=port) as mcr:
        mcr.command(f"enchant {player} {ench} {count}")


def best_time(adress="46.174.54.100", port=26576, password="LojSwh77x25e4c3SXMSUWvz23bWn5tM6"):
    with MCRcon(adress, password, port=port) as mcr:
        mcr.command("time set day")
        mcr.command("weather clear")


def check(adress="46.174.54.100", port=26576, password="LojSwh77x25e4c3SXMSUWvz23bWn5tM6y"):
    try:
        with MCRcon(adress, password, port=port) as mcr:
            return True
    except Exception as ex:
        return False


def start_mini_game(pl1, pl2, adress="46.174.54.100", port=26576, password="LojSwh77x25e4c3SXMSUWvz23bWn5tM6"):
    with MCRcon(adress, password, port=port) as mcr:
        mcr.command('fill 10 254 10 30 255 30 minecraft:bedrock')
        mcr.command(f'tp {pl1} 10 257 10')
        mcr.command(f'tp {pl2} 30 257 30')
        mcr.command("clear" + " " + pl1)
        mcr.command("clear" + " " + pl2)
        mcr.command("effect give " + pl1 + " speed 100 10")
        mcr.command("effect give " + pl1 + " regeneration 100 100")
        mcr.command("effect give " + pl2 + " regeneration 100 100")
        mcr.command("effect give " + pl2 + " speed 100 10")
        give_item(pl1, "stick{Enchantments:[{id:knockback,lvl:3}, {id:channeling,lvl:1}]}", 1)
        give_item(pl2, "stick{Enchantments:[{id:knockback,lvl:3}]}", 1)


with MCRcon("46.174.54.100", "LojSwh77x25e4c3SXMSUWvz23bWn5tM6", port=26576) as mcr:
    best_time()
    while True:
        eval(input())
