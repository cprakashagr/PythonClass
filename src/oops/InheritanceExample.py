class Base:

    def fun1Base(self):
        print('Fun1Base')

    def fun2Base(self):
        print('Fun2Base')

class Derived(Base):

    def fun1Derived(self):
        print('Fun2Derived')

    def fun2Base(self):
        # super(self)    # Throws Exception
        print('Fun2Derived')

if __name__ == '__main__':
    # obj = Base()
    # obj.fun1Base()

    obj2 = Derived()
    obj2.fun1Base()         # Parent's called
    obj2.fun1Derived()      # Self
    obj2.fun2Base()         # Child's called


    # Parent class visibility::
    print(Base.__bases__)


