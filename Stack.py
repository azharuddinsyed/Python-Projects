# Stacks
# Stack is LIFO (last in first out)
# Elements are always inserted at the top in the stack
# pop() will delete the element which was inserted recently
import sys


class Stack:
    stack = []
    stack_limit = 15

    def __init__(self, total_elem):
        self.total_elem = total_elem
        # fill the stack with elements

    # CREATE stack
    def fill_the_stack(self):
        for i in range(1, self.total_elem + 1):
            # self.stack.append(i)
            self.stack.insert(-i, i)
        print('Stack elements:', self.stack)

    # PUSH element
    def push_elem(self, pushelement):
        self.pushelement = pushelement
        if len(self.stack) > self.stack_limit:
            print("Stack is Full, Can't push more elements")
            sys.exit()
        self.stack.insert(0, self.pushelement)
        print("Element {} pushed to stack, new list is{}:".format(self.pushelement, self.stack))

    # POP element
    def pop_elem(self):
        if len(self.stack) == 0:
            print("No more elements in the stack to pop")
            sys.exit()
        print("Element {} is popped from stack, new list is{}".format(self.stack.pop(0), self.stack))
        # print("New list after pop:", self.stack)
        # self.list1.remove[0]


stack = Stack(10)
stack.fill_the_stack()

while True:
    print("Enter 1 for PUSH operation")
    print("Enter 2 for POP operation")
    print("Enter 3 to EXIT")

    user_input = int(input())

    if user_input == 1:
        print("Enter the element you want to PUSH:")
        user_input_1 = int(input())
        stack.push_elem(user_input_1)
    elif user_input == 2:
        stack.pop_elem()
    elif user_input == 3:
        break
        # quit()