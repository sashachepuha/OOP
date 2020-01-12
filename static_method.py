class someClass (object):
    @staticmethod               # дикоратор
    def someMethod():           # можно вызывать без создания экземпляра класса
        pass

someClass.someMethod() 
v = someClass()                 # создание экземпляра
v = someClass.someMethod()      # создание экземпляра в состоянии someMethod