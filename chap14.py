class Square:
    square_list = []
    
    def __init__(self, s):
        self.side = s
        self.square_list.append(self)

    def cal_perimeter(self):
        return self.side * 4

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)



def f(one, two):
    if one is two:
        return True
    else:
        return False
