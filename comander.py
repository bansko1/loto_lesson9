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

my_bill = Bill()
while True:
    print('Меню игры:')
    print('1 - Пополнить счет на сумму.')
    print('2 - Узнать сумму на счете.')
    print('3 - Играть в лотто.')
    #print('4 - Играть в лото.')
    print('5 - Закончить игру.')
    print('*************')
    choise = input('Выберите действие из списка выше - ')
    if choise == '1':
        count = int(input('Внесите на счет сумму:'))
        my_bill.add(count)
    if choise == '2':
        print(f'Сумма на счете {my_bill.money} единиц.')
    if choise == '3':
        my_bet = int(input('Сделайте ставку:'))
        my_bill.bet(my_bet)
        print(f'Вы играете в лотто. Ставка {my_bet} единиц.')
    #if choise == '4':
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
                    print(f'Цифры нет в карточке. Вы проиграли - ставка потеряна.')
                    break
                # Определяем есть ли в карточке число digit и убираем его в карточке игрока, если есть
                card_man.change(digit)
            if card_man.examin(digit):
                print('Цифра есть в карточке. Вы проиграли - ставка потеряна.')
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
                print(f'Вы выиграли. На счет добавлено {my_bet} единиц. Поздравляем!')
                my_bill.add(2*my_bet)
                break
            elif (card_men_1str or card_men_2str or card_men_3str) and not (
                    card_comp_1str or card_comp_2str or card_comp_3str):
                prn()
                print(f'Компьютер раньше. Вы проиграли - ставка потеряна. ')
                break
            elif not (
                    card_men_1str or card_men_2str or card_men_3str or card_comp_1str or card_comp_2str or card_comp_3str):
                prn()
                print(f'Ничья. {my_bet} единиц возвращены на счет.')
                my_bill.add(my_bet)
                break
    if choise == '5':
        print(f'Заканчиваем игру. На счете {my_bill.money} едениц.')
        break