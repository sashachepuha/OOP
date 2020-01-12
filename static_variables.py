class someClass(object):
    count = 0                        # статическая переменная (счетчик экземпляров)
    def __init__(self):
        self.__class__.count += 1    # изменяем статичискую переменную
                                     # при создании нового экземпляра класса
a = someClass()
a.count
b = someClass()
print(someClass.count)