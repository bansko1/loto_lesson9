class Bill:
    def __init__(self):
        self.money = 0
        print(f'Открываем счет {self}.')

    def add(self, count):
        self.money += count
        print(f'Вносим на счет {self} {count} единиц.')
    
    def bet(self, count):
        self.money -= count
        print(f'Со счета {self} делаем ставку на {count} единиц.')
    
    def resalt_of_bet(self, count):
        self.money += count
        print(f'Выигрыш/проигрыш по счету {self} составил {count} единиц. Счет изменен.')