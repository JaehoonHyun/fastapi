class Bag:

    tricks = []

    def __init__(self, name):
        print("I am bag")
        self.name = name
    
    def add_trick(self, trick):
        print("I am bag add_trick")
        self.tricks.append(trick)

    def show(self):
        print("I am bag show")


class Pocket:

    def __init__(self, name):
        print("I am pocket")
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        print("I am pocket add_trick")
        self.tricks.append(trick)

    def show(self):
        print("I am pocket show")


# 나 자신의 메소드부터 찾는다. BackPack -> Bag -> Pocket, 이렇게 하면 overriding부터 다이아몬드 상속관계까지 이해가능하다
class BackPack(Bag, Pocket) :
    def __init__(self, name):
        self.name = name


    def show(self):
        print("I am BackPack show")

if __name__ == "__main__" :
    b = BackPack('backpack')
    b.add_trick('bag? or pocket') #expected : I am bag add_trick
    b.show() #expected : I am BackPack show
