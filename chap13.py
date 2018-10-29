class Shape:
    def what_i_am(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def cal_perimeter(self):
        return self.width * 2 + self.len *2


class Square(Shape):
    def __init__(self, s):
        self.side = s

    def cal_perimeter(self):
        return self.side * 4

    def change_size(self, ns):
        self.side += ns

r = Rectangle(10,20)
s = Square(40)
r.what_i_am()
s.what_i_am()

class Horse:
    def __init__(self, n, c, r):
        self.name = n
        self.color = c
        self.rider = r

class Rider:
    def __init__(self, n, h, w):
        self.name = n
        self.hight = h
        self.weight = w

tsubasa = Rider("tsubasa", 166, 50)
aguro = Horse("aguro", "black",tsubasa)
print(aguro.rider.name)
