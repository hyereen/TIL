n = int(input())
sen = input()
del_idx = 0

for i in range(n):
    if i == 0:
        res = int(sen[0])
    if i % 2 == 1:
        del_idx = i + 1
        if sen[i] == '+':
            res = res + int(sen[i+1])
        elif sen[i] == '-':
            res = res - int(sen[i+1])
        elif sen[i] == '*':
            res = res * int(sen[i+1])
            print(res, int(sen[i+1]))
    if i == del_idx:
        continue
    
print(res)
    