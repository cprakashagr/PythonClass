from collections import deque;

if __name__ == "__main__":
    queue = deque()
    print (queue)
    queue.append(2)
    queue.append(4)
    queue.append(6)

    print (queue)

    queue.popleft()

    print (queue)

    queue.pop()

    print (queue)