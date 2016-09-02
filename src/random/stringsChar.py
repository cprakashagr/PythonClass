
def main():
    s = "Hello"
    print('--   Fetching as List   --')
    print (list(s))
    print('--   Fetching as Set   --')
    print (set(s))

    print('--   Direct iteration   --')
    for char in s:
        print(char)

    print('--   By Index   --')
    print(s[0])
    print(s[1])
    print(s[2])
    print(s[3])
    print(s[4])
    # print(s[5])   # IndexError

    print('--   By Iteration over length   --')
    for i in range(len(s)):
        print(s[i])

    print('--   Finding Index   --')
    firstIndex = s.index('l')
    print(firstIndex)
    print(s.index('k', firstIndex))


if __name__ == '__main__':
    main()
