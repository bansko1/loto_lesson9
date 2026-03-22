import random
from loto_oop import Random_map

param = 60  # сколько всего бочонков 30, 60, 90
cart_param = 12  # сколько чисел в карточке 9, 12, 15 (в три ряда по возрастанию)


card_man = Random_map(param, cart_param)
card_comp = Random_map(param, cart_param)

def prn():  # Распечатывание двух карточек
    print('***Ваша карточка***')
    card_man.print_card()
    print('*******************')
    print('Карточка компьютера')
    card_comp.print_card()
    print('*******************')

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
            print('Вы проиграли. Цифры нет в карточке')
            break
        # Определяем есть ли в карточке число digit и убираем его в карточке игрока, если есть
        card_man.change(digit)
    if card_man.examin(digit):
        print('Вы проиграли. Цифра есть в карточке')
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
        print('Вы выиграли. Поздравляем!')
        break
    elif (card_men_1str or card_men_2str or card_men_3str) and not (
            card_comp_1str or card_comp_2str or card_comp_3str):
        prn()
        print('Вы проиграли. Компьютер раньше.')
        break
    elif not (
            card_men_1str or card_men_2str or card_men_3str or card_comp_1str or card_comp_2str or card_comp_3str):
        prn()
        print('Ничья. Редкий случай.')
        break
