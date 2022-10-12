'''
Создайте программу для игры в ""Крестики-нолики"".
1 4 7
2 5 8
3 6 9
'''
a = [1, 5, 9]
b = [3, 5, 7]
c = [1, 2, 3]
d = [4, 5, 6]
g = [7, 8, 9]
m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(m))


def up(player, tabl):
    num = int(input(f'{player}, выбирете свободную клетку {tabl} '))
    return num


def game_start():
    player_on = ''
    user = ["player_x", "player_0"]
    tabl = []
    tabl = m
    while len(tabl) > 0:
        player_on = user.pop(0)
        tabl.remove(up(player_on, tabl))
        print(tabl)
        user.append(player_on)


game_start()
