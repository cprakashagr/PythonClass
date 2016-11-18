import pickle

'''

Pickeling is the process of converting a python object in to byte-stream and unpickling refers to the inverse process
where, a byte-stream is converted back to the python object hierarchy.

Pickling --- Serialization
Unpickling --- Deserialization

Certain Points for Pickle:

Marshal's Counter Part:
1. Maintains the reference to the objects it has already serialized
2. Have options to serialize the user defined classes


JSON counter part:
1. JSON is a text serialization format while Pickle is a binary serialization format.



DATA STREAM FORMAT:
-------------------
5 Protocols for pickling:
0 through 4.


'''


def main():
    print(pickle.DEFAULT_PROTOCOL)
    print(pickle.HIGHEST_PROTOCOL)

    '''

    dump()
    dumps()

    load()
    loads()

    '''

    pass

if __name__ == '__main__':
    main()
