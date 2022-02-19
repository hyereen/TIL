import sys
input = sys.stdin.readline # 시간초과나서 입력 받는 법 수정

n = int(input())
stack = []


def push(x):
    stack.append(x)


def pop():
    print(stack.pop(len(stack)-1))


def size():
    print(len(stack))


def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)


def top():
    print(stack[len(stack)-1])


for i in range(n):
    command_list = list(input().split())
    if len(command_list) != 1:
        command = command_list[0]
        num = int(command_list[1])
    else:
        command = command_list[0]

    if command == 'push':
        push(num)
    elif command == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            pop()
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            top()
