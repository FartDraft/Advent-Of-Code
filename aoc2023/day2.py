from re import compile

RED = compile(r"(\d+) red").findall
GREEN = compile(r"(\d+) green").findall
BLUE = compile(r"(\d+) blue").findall
GAME_NUM = compile(r"Game (\d+):").match

red = 12
green = 13
blue = 14

with open("a.txt") as f:
    total = 0
    for game in f.readlines():
        r = max(map(int, RED(game)))
        g = max(map(int, GREEN(game)))
        b = max(map(int, BLUE(game)))
        total += r * g * b

    print(total)
