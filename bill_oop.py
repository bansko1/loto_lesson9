class Bill:
    def __init__(self, name):
        self.name = name
        self.money = 0
        print(f'Открываем счет игрока {self.name}.')

    def __str__(self):
        return f'Счет игрока {self.name}'

    def add(self, count):
        self.money += count
        print(f'Вносим на {self} {count} единиц.')
    
    def bet(self, count):
        self.money -= count
        print(f'Со {self} делаем ставку на {count} единиц.')
    
    def resalt_of_bet(self, count):
        self.money += count
        print(f'Выигрыш/проигрыш по {self} составил {count} единиц. Счет изменен.')