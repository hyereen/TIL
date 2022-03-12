n = int(input())
num_list = list(map(int, input().split()))
num_list = sorted(num_list)

if n == 1:
    a = num_list[0] * num_list[0]
else:
    a = num_list[0] * num_list[n-1]
print(a)