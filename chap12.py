pop = []
jpop = []

def collect_songs():
    song = "曲名を入力してください："
    ask = "ｐかｊのどちらかを入力してください。ｑで終わります："
"""
    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)
        elif genre == "j":
            j = input(song)
            jpop.append(j)
        else:
            print("不正な入力です")

    print("pop songs:", pop)
    print("jpop songs:", jpop)

collect_songs()
"""

class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
        print("Created")

    def area(self):
        return self.width * self.len

    def change_size(self, w, l):
        self.width = w
        self.len = l


ra = Rectangle(10,20)
print(ra.area())
ra.change_size(20,40)
print(ra.area())
