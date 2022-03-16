class parent:
    def __init__(self):
        self.name = 'hyn'


class A(parent):
    def go(self):
        print(self.name)


class B(parent):
    def go(self):
        C = parent()
        A.go(C)


if __name__ == '__main__':
    b = B()
    b.go()
