import threading
import logging
import time


# logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')


def threadFunction(c = 1):
    logging.debug(c, 'Starting')
    print('Thread::::::::::', threading.currentThread().getName(), end='')
    print(c)
    logging.debug(c, 'Exiting')


def main():
    threadNameDict = {0: 'A', 1: 'B', 2: 'C'}
    threads = []
    for i in range(3):
        # t = threading.Thread(target=threadFunction(i))
        t = threading.Thread(name=threadNameDict[i], target=threadFunction(i))
        t.setName(i)
        threads.append(t)
        threads[i].start()

    # print(threads)
    # for i in range(3):
    #     pass

    for i in range(5000):
        print(i, end='')



if __name__ == '__main__':
    main()
