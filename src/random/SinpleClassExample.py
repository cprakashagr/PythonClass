class Hello:

    def __int__(self):
        print ('Constructor!')

    def function(self, x):
        print ('' + 'x')

    @staticmethod
    def staticMethod(x):
        if (x is not None):
            return 'Static method call' + str(x)

        else :
            return 'Static method call.'