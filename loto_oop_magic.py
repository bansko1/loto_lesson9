import random

"""Реализация игры в лото 2 игрока - человек играет с компьютером. 
Метод реализации - ООП
"""

param = 30  # сколько всего бочонков 30, 60, 90
cart_param = 9  # сколько чисел в карточке 9, 12, 15 (в три ряда по возрастанию)
list_vin = ['-', '-', '-']


class Random_map:  # Создание класса карточки лото

    def __init__(self, param, cart_param):  # Свойства класса карточки (содержание карточки)
        list_main = random.sample(list(range(1, param + 1)), cart_param)
        list_00 = list_main
        self.list_main = list_00
        list_01 = list_main[:cart_param // 3]
        list_01.sort()
        self.list_1 = list_01
        list_02 = list_main[cart_param // 3:cart_param // 3 * 2]
        list_02.sort()
        self.list_2 = list_02
        list_03 = list_main[cart_param // 3 * 2:]
        list_03.sort()
        self.list_3 = list_03

    def __str__(self):
        return f'{self.list_1[0]} {self.list_1[1]} {self.list_1[2]}' \
               f'\n{self.list_2[0]} {self.list_2[1]} {self.list_2[2]}' \
               f'\n{self.list_3[0]} {self.list_3[1]} {self.list_3[2]}'

    def __eq__(self, other):
        return self.list_main == other.list_main

    def __contains__(self, item):
        list_union = self.list_1 + self.list_2 + self.list_3
        return item in list_union

    def change(self, digit):  # Метод класса карточки
        '''
        проверка наличия цифры в карточке и замена ее на "-"
        :param digit: проверяем наличие этой цифры в карточке
        '''

        # [self.list_1[index] = '-' for index, item in enumerate(self.list_1) if item == digit]

        for index, item in enumerate(self.list_1):
            self.list_1[index] = '-' if item == digit else self.list_1[index]
            # if item == digit:
            #     self.list_1[index] = '-'
        for index, item in enumerate(self.list_2):
            self.list_2[index] = '-' if item == digit else self.list_2[index]
            # if item == digit:
            #     self.list_2[index] = '-'
        for index, item in enumerate(self.list_3):
            self.list_3[index] = '-' if item == digit else self.list_3[index]
            # if item == digit:
            #     self.list_3[index] = '-'


def prn():
    print('**Карточка игрока**')
    print(card_man)
    print('Карточка компьютера')
    print(card_comp)
    print('*******************')


if __name__ == "__main__":
    card_man = Random_map(param, cart_param)
    card_comp = Random_map(param, cart_param)

    if card_man == card_comp:
        print('Карточки одинаковые. Ничья.')
        breakpoint()
    else:
        print('Карточки разные. Играем с компьютером.')
    list_digit = list(range(1, param + 1))
    for n in range(param):  # Проход по всем бочонкам
        digit = random.choice(list_digit)
        list_digit.remove(digit)
        print(f'Новый бочонок: {digit}, (осталось {param - 1 - n})')
        prn()

        letter = input('Зачеркнуть цифру? (y/n)')
        if letter == 'y':
            if digit not in card_man:
                print('Вы проиграли. Цифры нет в карточке')
                break

            # Определяем есть ли в карточке число digit и убираем его в карточке игрока, если есть
            card_man.change(digit)
        if digit in card_man:
            print('Вы проиграли. Цифра есть в карточке')
            break
        # Определяем есть ли в карточке digit и убираем ее в карточке компьютера
        card_comp.change(digit)

        if (card_man.list_1 == list_vin and card_man.list_2 == list_vin and card_man.list_3 == list_vin) \
                and not (
                card_comp.list_1 == list_vin and card_comp.list_2 == list_vin and card_comp.list_3 == list_vin):
            prn()
            print('Вы выиграли. Поздравляем!')
            break
        elif (card_comp.list_1 == list_vin and card_comp.list_2 == list_vin and card_comp.list_3 == list_vin) \
                and not (card_man.list_1 == list_vin and card_man.list_2 == list_vin and card_man.list_3 == list_vin):
            prn()
            print('Вы проиграли. Компьютер закончил раньше.')
            break
        elif card_comp.list_1 == list_vin and card_comp.list_2 == list_vin and card_comp.list_3 == list_vin \
                and card_man.list_1 == list_vin and card_man.list_2 == list_vin and card_man.list_3 == list_vin:
            prn()
            print('Ничья. Редкий случай.')
            break
