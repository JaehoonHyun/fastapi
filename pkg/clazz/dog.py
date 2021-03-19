class Dog1:

    tricks = []

    def __init__(self, name):
        self.name = name
    
    def add_trick(self, trick):
        self.tricks.append(trick)

if __name__ == "__main__" :
    d = Dog1('abcd')
    e = Dog1('dd')
    d.add_trick('rolling out')
    e.add_trick('rooling back')

    #expected ['rolling out', 'rolling back']
    print(d.tricks)

class Dog2:

    def __init__(self, name):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)

if __name__ == "__main__" :
    d = Dog2('abcd')
    e = Dog2('dd')

    d.add_trick('rolling out')
    e.add_trick('rolling back')
    
    #expected ['rolling out']
    print(d.tricks)
