N = int(input())
s, g, p, d = map(int, input().split())
grades = list(input())

b_max = s -1
s_max = g -1
g_max = p -1
p_max = d -1
d_min = d

pay_sum = 0
pay_last = 0 # 지난달
pay_this = 0 # 이번달

for i in range(len(grades)):
    if grades[i] == 'B':
        pay_this = b_max - pay_last
    elif grades[i] == 'S':
        pay_this = s_max - pay_last
    elif grades[i] == 'G':
        pay_this = g_max - pay_last
    elif grades[i] == 'P':
        pay_this = p_max - pay_last
    elif grades[i] == 'D':
        pay_this = d_min

    pay_last = pay_this
    pay_sum = pay_sum + pay_this
    #print(grades[i], pay_this)

print(pay_sum)
