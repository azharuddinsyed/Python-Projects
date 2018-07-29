# Queue
# Queue is FIFO (first in first out)
# Elements are always inserted at the top in the queue
# pop() will delete the element at end of the queue

import sys


class Queue:
    queue = []
    queue_limit = 15

    def __init__(self, total_elem):
        self.total_elem = total_elem
        # fill the queue with elements

    # CREATE queue
    def fill_the_queue(self):
        for i in range(1, self.total_elem + 1):
            # self.queue.append(i)
            self.queue.insert(-i, i)
        print('Queue elements:', self.queue)

    # PUSH element - Adds an item to the top of the queue
    def push_elem(self, pushelement):
        self.pushelement = pushelement
        if len(self.queue) > self.queue_limit:
            print("Queue is Full, Can't push more elements")
            sys.exit()
            # return -1
        self.queue.insert(0, self.pushelement)
        print("Element {} pushed to queue, new list is{}:".format(self.pushelement, self.queue))

    # POP element - Removes item on top of the queue
    def pop_elem(self):
        if len(self.queue) == 0:
            print("No more elements in the queue to pop")
            sys.exit()
            # return -1
        print("Element {} is popped from queue, new list is{}".format(self.queue.pop(-1), self.queue))
        # print("New list after pop:", self.queue)
        # self.list1.remove[0]


queue = Queue(10)
queue.fill_the_queue()

while True:
    print("Enter 1 for PUSH operation")
    print("Enter 2 for POP operation")
    print("Enter 3 to EXIT")

    user_input = int(input())

    if user_input == 1:
        print("Enter the element you want to PUSH:")
        user_input_1 = int(input())
        queue.push_elem(user_input_1)
    elif user_input == 2:
        queue.pop_elem()
    elif user_input == 3:
        print("Good bye !!")
        break
        # quit()
