"""
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""

"""
import random
cand_on = 20


def cand_count(player, cand_of):
    cand = 0
    try:
        while cand > 28 or cand < 1 or cand > cand_of:
            cand = int(input(f'{player}, введите число от 1 до 28 и не более {cand_of} = '))
            print(f'{player} забрал {cand} конфет')
    except ValueError:
        print('Должно быть число, повторите попытку')
        exit()
    return cand


def cand_count_bot(player, cand_of):
    cand = 0
    if player == 'bot':
        while cand > 28 or cand < 1 or cand > cand_of:
            cand = random.randint(1, cand_of)
            print(f'bot забрал {cand} конфет')
        return cand
    else:
        try:
            while cand > 28 or cand < 1 or cand > cand_of:
                cand = int(input(f'{player}, введите число от 1 до 28 и не более {cand_of}  = '))
                print(f'{player} забрал {cand} конфет')
        except ValueError:
            print('Должно быть число, повторите попытку')
            exit()
        return cand


def game_start(bot):
    a = cand_on
    player_on = ' '
    if bot:
        user = ['player_1', 'bot']
        random.shuffle(user)
        while a > 0:
            player_on = user.pop(0)
            print(f'осталось конфет {a}')
            n = cand_count_bot(player_on, a)
            a -= n
            user.append(player_on)
        print(f'Победитель {player_on}')
    else:
        user = ['player_1', 'player_2']
        random.shuffle(user)
        while a > 0:
            player_on = user.pop(0)
            print(f'осталось конфет {a}')
            n = cand_count(player_on, a)
            a -= n
            user.append(player_on)
        print(f'Победитель {player_on}')


game_start(int(input('Режим против игрока 0, против бота 1. Выберите режим : ')))




