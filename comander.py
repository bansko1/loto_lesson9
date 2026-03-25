from datetime import datetime
import json
import os
import random
from loto_oop import Random_map
from bill_oop import Bill

def prn():  # Распечатывание двух карточек
    print('***Ваша карточка***')
    card_man.print_card()
    print('*******************')
    print('Карточка компьютера')
    card_comp.print_card()
    print('*******************')

FILE_NAME = 'bills.json'
FILE_HISTORY = 'histores.json'

bills = {}
histores = []

if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            bills = json.load(f)
if os.path.exists(FILE_HISTORY):
        with open(FILE_HISTORY, 'r') as f:
            histores = json.load(f)

while True:
    print('Меню игры:')
    print('1 - Проверить есть ли счет у игрока. Если есть - открыть его, если нет - создть счет.')
    print('2 - Пополнить счет на сумму.')
    print('3 - Узнать сумму на счете.')
    print('4 - История счета.')
    print('5 - Играть в лотто.')
    print('6 - Закончить игру.')
    print('*************')
    choise = input('Выберите действие из списка выше - ')
    if choise == '1': # Открытие счета
        name = input('Введите имя игрока:')
        if name not in bills:
            now = datetime.now().strftime("%d-%m-%Y")
            bill = Bill(name)
            count = int(input(f'Внесите сумму:'))
            bill.money = count
            bills[name] = count
            print(f'Игроку {name} открыт счет на {count} единиц.')
            history = f'{now} открыт {bill.name} на {count} единиц.'
            histores.append(history)
            with open(FILE_HISTORY, 'w') as f:
               json.dump(histores, f)
        else:
            bill = Bill(name)
            bill.money = bills[name]
            print(f'У игрока {name} есть счет на {bills[name]} единиц.')
        
    if choise == '2': # Пополнить счет.
        count = int(input(f'Внесите сумму:'))
        bill.add(count)
        bills[bill.name] = bill.money
        now = datetime.now().strftime("%d-%m-%Y")
        history = f'{now} {bill} пополнен на {count} единиц.'
        histores.append(history)
        with open(FILE_HISTORY, 'w') as f:
           json.dump(histores, f)
    if choise == '3': # Узнать сумму на счете.
        name = input('Введите имя игрока:')
        if name not in bills:
            print(f'У {name} нет счета.')
        else:
            print(f'Остаток на {bill} - {bill.money} единиц.')

    if choise == '4': # История счета
        with open(FILE_HISTORY, 'r') as f:
            resalt = json.load(f)
        print(f'История {bill}:')
        print(resalt)
    if choise == '5':
        if bill.money == 0:
            print(f'Игра в долг не допускается. Пополните {bill}.')
            #count = int(input(f'Внесите на {bill} сумму:'))
            #if count <= bill.money:
            #    print(f'Заканчиваем игру. Долг по {bill} - {bill.money} едениц. Игра с долгом не допускается.')
            #    bills[bill.name] = bill.money
            #    with open(FILE_NAME, 'w') as f:
            #        json.dump(bills, f)
            break
            bill.add(count)
        my_bet = int(input(f'Сделайте ставку не более чем {bill.money}:'))
        if my_bet > bill.money:
            print(f'Пополните {bill}')
            #count = int(input(f'Внесите сумму не менее {my_bet - bill.money} :'))
            #bill.add(count)
            #if count < my_bet - bill.money:
            #    print(f'На {bill} внесено недостаточно.')
            #    print(f'Заканчиваем игру. Остаток на {bill} составляет {bill.money} едениц.')
            #    bills[bill.name] = bill.money
            #    with open(FILE_NAME, 'w') as f:
            #        json.dump(bills, f)
            break
            
        bill.bet(my_bet)
        print(f'Игрок {bill.name} играет в лотто. Ставка {my_bet} единиц принята.')

        param = 30  # сколько всего бочонков 30, 60, 90
        cart_param = 9  # сколько чисел в карточке 9, 12, 15 (в три ряда по возрастанию)

        card_man = Random_map(param, cart_param)
        card_comp = Random_map(param, cart_param)

        list_digit = list(range(1, param + 1))
        for n in range(param):  # Проход по всем бочонкам
            digit = random.choice(list_digit)
            list_digit.remove(digit)
            print(f'Новый бочонок: {digit}, (осталось {param - 1 - n})')
            prn()

            letter = input('Зачеркнуть цифру? (y/n)')
            if letter == 'y':
                if not card_man.examin(digit):
                    # print(not card_man.change(digit))
                    print(f'Цифры нет в карточке. {bill.name} проиграл - ставка потеряна.')
                    now = datetime.now().strftime("%d-%m-%Y")
                    history = f'{now} Проигрыш в лото - зачеркнутой цифры нет в карточке. {bill} уменьшен на {my_bet} единиц.'
                    histores.append(history)
                    with open(FILE_HISTORY, 'w') as f:
                        json.dump(histores, f)
                    break
                # Определяем есть ли в карточке число digit и убираем его в карточке игрока, если есть
                card_man.change(digit)
            if card_man.examin(digit):
                print(f'Цифра есть в карточке. {bill.name} проиграл - ставка потеряна.')
                now = datetime.now().strftime("%d-%m-%Y")
                history = f'{now} Проигрыш в лото - не зачеркнута цифра в карточке. {bill} уменьшен на {my_bet} единиц.'
                histores.append(history)
                with open(FILE_HISTORY, 'w') as f:
                    json.dump(histores, f)                
                break
            # Определяем есть ли в карточке digit и убираем ее в карточке компьютера
            card_comp.change(digit)

            # Проверяем условия окончания игры
            card_men_1str = card_man.list_1
            card_men_2str = card_man.list_2
            card_men_3str = card_man.list_3
            card_comp_1str = card_comp.list_1
            card_comp_2str = card_comp.list_2
            card_comp_3str = card_comp.list_3

            if not (card_men_1str or card_men_2str or card_men_3str) and (
                    card_comp_1str or card_comp_2str or card_comp_3str):
                prn()
                print(f'{bill.name} выиграл {my_bet} + {my_bet} единиц. Поздравляем!!!')
                bill.add(2*my_bet)
                now = datetime.now().strftime("%d-%m-%Y")
                history = f'{now} Выигрыш в лото. {bill} увеличен на {my_bet} единиц.'
                histores.append(history)
                with open(FILE_HISTORY, 'w') as f:
                    json.dump(histores, f)
                break
            elif (card_men_1str or card_men_2str or card_men_3str) and not (
                    card_comp_1str or card_comp_2str or card_comp_3str):
                prn()
                print(f'Компьютер раньше. {bill.name} проиграл - ставка потеряна. ')
                now = datetime.now().strftime("%d-%m-%Y")
                history = f'{now} Проигрыш в лото - компьютер зачеркнул раньше. {bill} уменьшен на {my_bet} единиц.'
                histores.append(history)
                with open(FILE_HISTORY, 'w') as f:
                    json.dump(histores, f)                
                break
            elif not (
                    card_men_1str or card_men_2str or card_men_3str or card_comp_1str or card_comp_2str or card_comp_3str):
                prn()
                print(f'Ничья. Ставка возвращается.')
                now = datetime.now().strftime("%d-%m-%Y")
                history = f'{now} Ньчья - все цифры зачеркнуты одновременно. {bill} не меняется.'
                histores.append(history)
                with open(FILE_HISTORY, 'w') as f:
                    json.dump(histores, f)
                bill.add(my_bet)
                break
            
    if choise == '6':
        print(f'Заканчиваем игру. На {bill} остаток {bill.money} едениц.')
        bills[bill.name] = bill.money
        with open(FILE_NAME, 'w') as f:
            json.dump(bills, f)
        break