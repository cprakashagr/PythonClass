
def func():
    yield 1
    yield 2
    yield 3


def main():
    for item in func():
        print(item)
    # print(func())    #<generator object func at 0x7f227f3ae3b8>

    obj1 = (1,2,3,)

    obj = (i for i in range(10))
    print (obj)
    # print(obj[1])     # 'generator' object is not subscriptable

    obj2 = [i for i in range(10)]
    print(obj2)
    print(obj2[1])      # Works absolutely fine

    mygenerator = (x*x for x in range(3))
    print(mygenerator)

    print('-------')
    print('Iterate A Generator')
    print('-------')
    for item in obj:
        print(item)

    print('-------')
    print('Again!!!')
    print('-------')
    for item in obj:
        print(item)              # Prints nothing

if __name__ == '__main__':
    main()
