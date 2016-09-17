

def main():

    lM = lambda arg: arg * 2

    print(lM(5))    # 10
    print(lM(0))    # 0
    print(lM(10))   # 20

    my_list = [1, 5, 4, 6, 8, 11, 3, 12]

    new_list = list(filter(lambda x: (x%2 == 0), my_list))
    print(new_list)

    pass

if __name__ == "__main__":
    main()