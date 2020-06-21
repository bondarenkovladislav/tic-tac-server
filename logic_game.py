# -*- coding: utf-8 -*-
import sys
from logic_game_class import Game

def enter_coordinates(game_s, name, x_coordinate, y_coordinate):
    # """Проверяем пришедшие координаты"""
    if ((x_coordinate > 2 or x_coordinate < 0) or (y_coordinate >2 and y_coordinate < 0)):
        print("Error, the coordinate is already occupied")
        return {"status":'filled', "result": None}
    elif (name != game_s.user_1 and name != game_s.user_2):
        print("Error, the user is not found")
        return {"status": 'user_not_found', "result": None}
    elif (game_s.field_of_play[x_coordinate][y_coordinate] != 0):
        print("Error, the coordinate is already occupied")
        return {"status": 'filled', "result": None}
    elif (((game_s.number_of_moves % 2 == 0) and (name == game_s.user_2)) or
          ((game_s.number_of_moves % 2 != 0) and (name == game_s.user_1))):
        print("Error, another player is walking")
        return {"status": 'wrong_order', "result": None}
    else:
        victory = fill_field(game_s, name, x_coordinate, y_coordinate) # эту строку вообще удалить, она для теста
        if victory != None:
            return {"status": 'victory', "winner": victory}
        #!!! Нужно вызвать метод fill_field(name, x_coordinate, y_coordinate), если пришел ответ ""ОК"""
        return {"status": 'OK', "result": None}


def fill_field(game_s, name, x_coordinate, y_coordinate):
    """заводим координаты в массив игрового поля"""
    if (name == game_s.user_1):
        game_s.field_of_play[x_coordinate][y_coordinate] = 1
        game_s.number_of_moves += 1
        return result_game(game_s)
    elif (name == game_s.user_2):
        game_s.field_of_play[x_coordinate][y_coordinate] = 2
        game_s.number_of_moves += 1
        return result_game(game_s)

def result_game(game_s):
    field = game_s.field_of_play
    flag = 0
    i = 0
    while (i <= 2):
        j = 0
        while (j <= 2):
            if (field[i][j] == 0):
                flag = 1
            j += 1
        i += 1
    if (flag == 0):
        return game_s.victory(3)
    #Сравниваем по строкам
    if (field[0][0] != 0 and field[0][0] == field[0][1] == field[0][2]):
        return game_s.victory(field[0][0])
    elif (field[1][0] != 0 and field[1][0] == field[1][1] == field[1][2]):
        return game_s.victory(field[1][0])
    elif (field[2][0] != 0 and field[2][0] == field[2][1] == field[2][2]):
        return game_s.victory(field[2][0])
    #Сравниваем по столбцам
    elif (field[0][0] != 0 and field[0][0] == field[1][0] == field[2][0]):
        return game_s.victory(field[0][0])
    elif (field[0][1] != 0 and field[0][1] == field[1][1] == field[2][1]):
        return game_s.victory(field[0][1])
    elif (field[0][2] != 0 and field[0][2] == field[1][2] == field[2][2]):
        return game_s.victory(field[0][2])
    #Сравниваем диагонали
    elif (field[0][0] and field[0][0] == field[1][1] == field[2][2]):
        return game_s.victory(field[0][0])
    elif (field[2][0] and field[2][0] == field[1][1] == field[0][2]):
        return game_s.victory(field[2][0])
    return None

# def process_command(game_s, command):
#     """Выполняет действие, в зависимости от выбранной команды"""
#     if (command == '-1'):
#         print()
#     elif (command == '2'):
#         enter_coordinates(input("Enter user's name: "), int(input("Enter x: ")), int(input("Enter y: ")))# в этот метод передать имя и координаты хода игроков
#
#     elif (command == '3'):
#         game_s.vivod()
#     return

# def start():
def startGame(user1, user2):
    return Game(user1,
                  user2)  # сюда передать имена, вместо ввода из консоли
# user_comand = '-2'
# while user_comand != '-1':
#     user_comand = input("Выберите действие (2-ввести новые координаты) (3-посмотреть разультат заполнения поля) (-1-выйти): ")
#     process_command(user_comand)
