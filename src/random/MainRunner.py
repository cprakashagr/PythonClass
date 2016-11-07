from .SinpleClassExample import Hello
from src.ds.ll import *


if __name__ == "__main__":
    object = Hello()
    object.function(2)
    object.function(4)

    of = object.staticMethod

    object.function('ABC DEF GHI JKL')
    object.function("ABC")

    # Hello.staticMethod(object)
    # Hello.staticMethod(56)
    # Hello.staticMethod('Hello')
    object.item = 45
    print (object.item)

    print ('Function referrence demo: ' + of('None'))

    newList = UnOrderedLinkedList()
    newList.addNode(Node(43))
    newList.addNode(Node('Hello'))

    newList.printAll()

