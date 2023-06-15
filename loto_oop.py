import random

"""Реализация игры в лото 2 игрока - человек играет с компьютером. 
Метод реализации - ООП
"""

param = 30  # сколько всего бочонков 30, 60, 90
cart_param = 9  # сколько чисел в карточке 9, 12, 15 (в три ряда по возрастанию)


class Random_map:  # Создание класса карточки лото

    def __init__(self):  # Свойства класса карточки (содержание карточки)
        list_main = random.sample(list(range(1, param + 1)), cart_param)
        # print(list_main)
        list_01 = list_main[:cart_param // 3]
        list_01.sort()
        self.list_1 = list_01
        list_02 = list_main[cart_param // 3:cart_param // 3 * 2]
        list_02.sort()
        self.list_2 = list_02
        list_03 = list_main[cart_param // 3 * 2:]
        list_03.sort()
        self.list_3 = list_03

    def examin(self, digit):  # Метод возвращает True, если digit есть в карточке
        list_union = self.list_1 + self.list_2 + self.list_3
        return digit in list_union

    def change(self, digit):  # Метод класса карточки
        '''
        проверка наличия цифры в карточке и удаление ее из карточки
        :param digit: проверяем наличие этой цифры в карточке
        :return: возвращаем новые строчки карточки
        '''
        if digit in self.list_1:
            self.list_1.remove(digit)
        elif digit in self.list_2:
            self.list_2.remove(digit)
        elif digit in self.list_3:
            self.list_3.remove(digit)

    def print_card(self):  # Метод класса карточки
        '''
        распечатка карточки
        :return:
        '''
        print(" ".join(map(str, self.list_1)))
        print(" ".join(map(str, self.list_2)))
        print(" ".join(map(str, self.list_3)))


def prn():  # Распечатывание двух карточек
    print('***Ваша карточка***')
    card_man.print_card()
    print('*******************')
    print('Карточка компьютера')
    card_comp.print_card()
    print('*******************')


card_man = Random_map()
card_comp = Random_map()

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
