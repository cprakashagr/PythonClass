import hashlib


def main():
    print(hashlib.algorithms_available)
    print(hashlib.algorithms_guaranteed)
    enc = hashlib.sha512("AB".encode())
    print(enc.hexdigest())
    print(len(enc.hexdigest()))


    hash_object = hashlib.new('DSA')
    hash_object.update("Hello".encode())
    print(hash_object.hexdigest())
    print(len(hash_object.hexdigest()))

if __name__ == "__main__":
    main()