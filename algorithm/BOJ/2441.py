n = int(input())
j = 0
for i in range(n, 0, -1):
    star = "*"
    blank = " "
    print(blank*j + star*i)
    j += 1