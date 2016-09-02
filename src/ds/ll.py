class UnOrderedLinkedList:

    start = None
    current = None
    size = 0

    def addNode(self,node):

        if self.start is None:
            self.start = node

        if self.current is None:
            self.current = node
        else:
            self.current.next = node
            self.current = node

        self.size += 1

    def removeSingleNode(self, node, all = False):

        if self.start is None:
            raise UnOrderedLinkedListException('Underflow')

        local = self.start
        if self.start.data == node.data:
            self.start = self.start.next
            del local

        else:
            parent = local
            while local.next is not None:
                if local.next.data == node.data:
                    local.next = local.next.next
                    del parent
                    if all is True:
                        break

                parent = local
                local = local.next

        pass

    def removeAllNodes(self, node):

        self.removeSingleNode(node, True)

        pass

    def printAll(self):
        if self.start is None:
            pass
        else:
            local = self.start
            while local is not None:
                print (local.data)
                local = local.next


class UnOrderedLinkedListException(Exception):

    def __init__(self, message):
        self.message = message

    def getMessage(self):
        return self.message

    pass


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNode(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNode(self, nextNode):
        self.next = nextNode

if __name__ == '__main__':

    globalList = UnOrderedLinkedList()

    globalList.addNode(Node(2))
    globalList.addNode(Node(5))
    globalList.addNode(Node(6))
    globalList.addNode(Node(5))
    globalList.addNode(Node(56))
    globalList.addNode(Node(7))

    try:
        globalList.removeAllNodes(Node(5))
    except UnOrderedLinkedListException as e:
        print (e.message)

    globalList.printAll()
