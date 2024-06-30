'''Задача "Developer - не только разработчик":
Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
Пункты задачи:
Создайте класс House.
Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные значения.
Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
Создайте объект класса House с произвольным названием и количеством этажей.
Вызовите метод go_to у этого объекта с произвольным числом.

Пример результата выполнения программы:
Исходные данные:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
'''

# и задача №2:

'''
Цель: понять как работают базовые магические методы на практике.

Задача "Магические здания":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".

Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

Пример результата выполнения программы:
Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20'''

class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.nFloors = number_of_floors

    def go_to(self, new_floor: int):
        if new_floor > self.nFloors:
            print('Такого этажа не существует!')
        else:
            if new_floor < 1:
                for f in range(1, new_floor-1, -1):
                    print('Спускаемся:', f)
            for f in range(1, new_floor+1):
                print('Поднимаемся:', f)

    def __len__(self):
        return self.nFloors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.nFloors}.'

def main():
    # №1
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h3 = House('ЖК Летний', 22)
    h1.go_to(5)
    h2.go_to(10)
    h3.go_to(-2)
    # №2
    print(f'ДЗ-2: {h1}, {h2}, {h3}')
    print(len(h1), len(h2), len(h3))

if __name__ == '__main__':
    main()