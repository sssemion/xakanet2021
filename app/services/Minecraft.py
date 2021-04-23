from mcrcon import MCRcon
from random import randint

#
# def give_effect(player, effect, duration, s, adress, port,
#
#     with MCRcon(adress, password, port=port) as mcr:
#         a = mcr.command("effect give" + player + " " + effect + str(duration) + " " + str(s))
#         print(a)


def give_item(player, item, count, adress, port, password):
    with MCRcon(adress, password, port=port) as mcr:
        c = mcr.command(f"give {player} {item} {count}")
        return c[:4] == "Gave"


def best_time(adress, port, password):
    with MCRcon(adress, password, port=port) as mcr:
        mcr.command("time set day")
        mcr.command("weather clear")


def check(adress, port, password):
    try:
        with MCRcon(adress, password, port=port) as mcr:
            return True
    except Exception as ex:
        return False


def start_mini_game(pl1, pl2, adress, port, password):
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
        a = mcr.command("give " + pl1 + " stick{Enchantments:[{id:knockback,lvl:3}]}" + " 1")
        b = mcr.command("give " + pl2 + " stick{Enchantments:[{id:knockback,lvl:3}]}" + " 1")
        return [a[:4] == b[:4] == " Gave"]


def sand_lock(pl, adress, port, password):
    with MCRcon(adress, password, port=port) as mcr:
        a = mcr.command(f"execute at {pl} run fill ~-2 ~-2 ~-2 ~2 ~2 ~2 minecraft:sand")
        return a[:12] == 'Successfully'


def web_lock(pl, adress, port, password):
    with MCRcon(adress, password, port=port) as mcr:
        a = mcr.command(f"execute at {pl} run fill ~-2 ~-2 ~-2 ~2 ~2 ~2 minecraft:web")
        return a[:12] == 'Successfully'


def mega_bomb(pl, adress, port, password):
    with MCRcon(adress, password, port=port) as mcr:
        a = mcr.command('execute at ' + pl + ' run summon creeper ~ ~ ~ {powered:1, count:3} ')
        return a[:8] == "Summoned"


def lighting(pl, adress, port, password):
    with MCRcon(adress, password, port=port) as mcr:
        for i in range(3):
            a = mcr.command('execute at ' + pl + ' run summon minecraft:lightning_bolt ~ ~ ~')
        return a[:8] == "Summoned"


with MCRcon("46.174.54.100", "LojSwh77x25e4c3SXMSUWvz23bWn5tM6", port=26576) as mcr:
    while True:
        eval(input())
