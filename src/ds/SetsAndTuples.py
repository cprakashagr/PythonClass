

if __name__ == '__main__':
    a = 2,4
    b = 1,
    c = b
    d = c
    # a, b = c, d

    print(c)
    print(d)

    a, b = b, a
    print(a, b)

    # Sets contains non duplicate items
