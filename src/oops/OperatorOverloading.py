class Hello:

    def __init__(self, d):
        self.data = d

    def __gt__(self, other):
        if isinstance(other, Hello):
            return self.data > other.data

        elif isinstance(other, (int, float)):
            return self.data > other

        else:
            return NotImplemented

    pass

if __name__ == '__main__':
    h1 = Hello(2)
    h2 = Hello(2)

    if h1>h2:
        print('H1')

    else:
        print('H2')
