from __future__ import with_statement


class WithExample:

    def __init__(self):
        print('Ho Ho')

    def __enter__(self):
        print('Ha ha')
        # self.__exit__(1,2,3)     // Calls the __exit__ on top of all functions stack..  Will be called again by
        # the PyInterpreter

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('He He')
        print(exc_tb)
        print(exc_val)
        print(exc_type)

if __name__ == '__main__':

    with WithExample() as w:
        pass
