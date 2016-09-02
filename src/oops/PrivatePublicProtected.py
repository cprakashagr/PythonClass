class ModifierExample:

    def __init__(self):
        self.someVariable = 10
        #Constructors

    def someFunction(self, x):
        self.__anotherVariable = x


if __name__ == '__main__':
    obj1 = ModifierExample()
    obj1.someFunction(50)
    print(obj1.someVariable)
    print(obj1.__dict__.clear())

    #print obj1.__anotherVariable   # Not accessible

    obj2 = ModifierExample()
    obj2.someFunction(60)

    print(obj2.__dict__.get('_ModifierExample__anotherVariable'))  # Gets accessible.

    objExample = {}
    # print type(objExample).__module__
    print(obj1.__module__ ) # Prints __main__
    print(obj1.__class__)   # Prints ModifierExample


