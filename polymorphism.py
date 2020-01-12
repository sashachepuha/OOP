# ПРИМЕР ПОЛИМОРФИЗМА

class vector(object):
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            # если значение число
            return vector(
                self.x * other,
                self.y * other,
                self.z * other
            )
        elif isinstance(other, vector):
            # если значение вектор
            return vector(
            self.x * other.x,
            self.y * other.y,
            self.z * other.z
            )
    def __repr__(self):
        return 'Vector - %s:%s:%s' % (self.x, self.y, self.z)  
v1 = vector(1, 2, 3)
v2 = vector(2, 3, 4)
v3 = v1 * v2
print(v3)