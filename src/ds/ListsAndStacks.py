# var3 = 'Hello';
# print var3;
# var3 = 6;
# print var3;
# print var3;

import sys

if __name__ == "__main__":
    listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(listA)
    listA.append(1)
    print(listA)
    print(listA.insert(2, 12))
    print(listA)
    # listA.sort(reverse=True)  # Descending
    # listA.sort(reverse=False) # Ascending
    listA.sort()                # Ascending by default
    print(listA)

    # Stack
    st = []
    st.append(1)
    st.append(2)

    print (st)

    flag = True
    # while st.count(st) > 0: #True
    #     try:
    #         st.pop()
    #         print st
    #
    #         #  raise NameError('Hi There');
    #
    #     except:
    #         print 'Can\'t Pop', sys.exc_info()[0]
    #         flag = False
    #         break

    # Sets


    delList = [0,1,2,3,4,5,6,7,8,9,10]
    delList2 = delList

    print(delList)
    print(delList2)

    del delList[0]
    print(delList)
    del delList[2:4]
    print(delList)

    del delList[:]
    print(delList)   # Empty List

    del delList2
    print(delList2)  # Error as variable is deleted
