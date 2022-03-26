from collections import deque

lst = deque()
record = []
A, P = map(int, input().split())

lst.append(A)
record.append(A)

# 제곱함수 만들기에서 잘못생각해서 틀렸었다 !
def P_double(p, n):
    p = p - 1
    if p == 0:
        return n
    return P_double(p, n) * n


while True:
    # print(record, "record")
    cur_num = lst.popleft()
    # print(cur_num)
    double = 0
    for i in list(str(cur_num)):
        intnum = int(i)
        double = double + P_double(P, intnum)
    # print(double, "double")
    if double in record:
        print(len(record[:record.index(double)]))
        break
    lst.append(double)
    record.append(double)
