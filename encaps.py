class divider (object):
    def __init__(self):
        self.__div = 10
        # скрываем от изменения перемееную div по средствам "__"

    def division (self, value):
        print(value / self.__div)

    def setDivider (self, val):
        if self.__checkValue(val):
            self.__div = val
        else:
            print('Делитель должен быть больше нуля')

    def __checkValue (self, val):
        return not val == 0

d = divider()
d.setDivider(int(input('Введите делитель: ')))
d.division(int(input('Введите число: ')))