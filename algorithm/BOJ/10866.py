import sys
input = sys.stdin.readline # 시간초과 해결 방법

n = int(input())
stack = []

def push_front(x):
    stack.insert(0, x)

def push_back(x):
    stack.append(x)


def pop_front():
    print(stack.pop(0))

def pop_back():
    print(stack.pop(len(stack)-1))


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def front():
    print(stack[0])

def back():
    print(stack[len(stack)-1])


for i in range(n):
    command_list = list(input().split())
    if len(command_list) != 1:
        command = command_list[0]
        num = int(command_list[1])
    else:
        command = command_list[0]

    if command == 'push_front':
        push_front(num)
    elif command == 'push_back':
        push_back(num)
    elif command == 'pop_front':
        if len(stack) == 0:
            print(-1)
        else:
            pop_front()
    elif command == 'pop_back':
        if len(stack) == 0:
            print(-1)
        else:
            pop_back()
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            front()
    elif command == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            back()
