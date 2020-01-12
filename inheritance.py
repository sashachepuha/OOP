# ПРИМЕР НАСЛЕДОВАНИЯ

class PC (object):
    def __init__(self):
        self.model =''
        self.speed = ''

    def ShowSpeed (self):
        print(self.speed + self.model)

class Laptop (PC):
    # Наследуем клас Laptop от класса PC
    def __init__(self):
        super(Laptop, self).__init__()
        # функция super() пробежит по всемродителям класса Laptop
        # и добавит все свойства __init__ не дублируя

    def ShowSpeed (self):
        # создаем такую же функцию как у родителя
        if True:
            pass
            # новые действия для функции
        else:
            super(Laptop, self).ShowSpeed()
            # выполняем функцию родителя
    def ShowModel(self):
        print('Laptop')
