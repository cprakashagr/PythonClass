from .SinpleClassExample import Hello

if __name__ == '__main__':
    dic = {'key1':'1', 'key2':'2'}      # No Duplicate Keys allowed. Last one to override the all

    for key in dic:
        print(key)
        print(dic.get(key))

    obj1 = Hello()
    obj2 = Hello()


    # Object Dictionaries

    objDict = {}
    objDict['key01'] = obj1   # Location
    objDict['key02'] = obj2

    print (objDict)
