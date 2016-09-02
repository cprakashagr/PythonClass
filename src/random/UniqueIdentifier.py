from .SinpleClassExample import Hello

if __name__ == '__main__':

    for i in range(0, 5):
        obj = Hello()
        print (id(obj))

    '''
    39795160
    39796312
    39795160
    39796312
    39795160
    39796312
    39795160
    39796312
    39795160
    39796312
    '''

    for i in range(0, 5):
        print (id(Hello()))

    '''
    53975768
    53975768
    53975768
    53975768
    53975768
    53975768
    53975768
    53975768
    53975768
    53975768
    '''

    obj1 = Hello(); obj2 = Hello(); obj3 = Hello(); obj4 = Hello(); obj5 = Hello()

    print(id(obj1)); print(id(obj2)); print(id(obj3)); print(id(obj4)); print(id(obj5))

    '''
    140358562285400
    140358562285328
    140358562310552
    140358562310624
    140358562310696
    '''