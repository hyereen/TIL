n = int(input())

for i in range(1, n+1):
    star = "*"
    blank = " "
    print(blank*(n-i)+star*(2*i-1)) # 뒤쪽에는 blank가 필요하지않다!!!
