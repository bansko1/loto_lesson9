import random

"""Реализация игры в лото 2 игрока - человек играет с компьютером. 
Метод реализации - процедурное программирование
"""

param = 30  # сколько всего бочонков 30, 60, 90
cart_param = 9  # сколько чисел в карточке 9, 12, 15 (располагаются в три ряда по возрастанию)


def creation(param, cart_param):  # Функция создания карточки
    list_main = random.sample(list(range(1, param + 1)), cart_param)
    # print(list)
    list_1 = list_main[:cart_param // 3]
    list_1.sort()
    # print(list_1)
    list_2 = list_main[cart_param // 3:cart_param // 3 * 2]
    list_2.sort()
    # print(list_2)
    list_3 = list_main[cart_param // 3 * 2:]
    list_3.sort()
    return list_1, list_2, list_3


def prnt(list_11, list_12, list_13, list_21, list_22, list_23):
    print('----- Ваша карточка -----')
    print(" ".join(map(str, list_11)))
    print(" ".join(map(str, list_12)))
    print(" ".join(map(str, list_13)))
    print('-------------------------')

    print('-- Карточка компьютера --')
    print(" ".join(map(str, list_21)))
    print(" ".join(map(str, list_22)))
    print(" ".join(map(str, list_23)))
    print('-------------------------')

if __name__ == "__main__":
    list_11, list_12, list_13 = creation(param, cart_param)
    list_21, list_22, list_23 = creation(param, cart_param)

    list_digit = list(range(1, param + 1))
    # print(list_digit)

    for n in range(param):
        digit = random.choice(list_digit)
        list_digit.remove(digit)
        print(f'Новый бочонок: {digit}, (осталось {param - 1 - n})')

        prnt(list_11, list_12, list_13, list_21, list_22, list_23)

        letter = input('Зачеркнуть цифру? (y/n)')
        if letter == 'y':
            # Определяем есть ли в карточке digit и убираем ее (в обеих карточках)
            if digit in list_11:
                list_11.remove(digit)
            elif digit in list_12:
                list_12.remove(digit)
            elif digit in list_13:
                list_13.remove(digit)
            else:
                print('Вы проиграли')
                break
            if digit in list_21:
                list_21.remove(digit)
            elif digit in list_22:
                list_22.remove(digit)
            elif digit in list_23:
                list_23.remove(digit)
            prnt(list_11, list_12, list_13, list_21, list_22, list_23)
        else:
            # Проверяем, что в карточке игрока нет digit. Если ошибка - завершение с проигрышем
            if digit in list_11:
                print('Вы проиграли')
            elif digit in list_12:
                print('Вы проиграли')
            elif digit in list_13:
                print('Вы проиграли')

            if digit in list_21:
                list_21.remove(digit)
            elif digit in list_22:
                list_22.remove(digit)
            elif digit in list_23:
                list_23.remove(digit)
            prnt(list_11, list_12, list_13, list_21, list_22, list_23)
        # else:
        #     print('Повторите ввод')
        if not (list_11 or list_12 or list_13) and (list_21 or list_22 or list_23):
            print('Вы выиграли. Поздравляем!')
            break
        elif (list_11 or list_12 or list_13) and not (list_21 or list_22 or list_23):
            print('Вы проиграли. Компьютер раньше.')
            break
        elif not (list_11 or list_12 or list_13 or list_21 or list_22 or list_23):
            print('Ничья. Редкий случай.')
            break