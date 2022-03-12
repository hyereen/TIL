num_list = []
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        num_list.append(n)

if len(num_list) == 0:
    print(-1)
else:
    num_list = sorted(num_list)
    print(sum(num_list))
    print(num_list[0])
