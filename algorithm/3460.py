t = int(input())

for i in range(t):
    n = int(input())
    n_list = list(format(n, 'b'))
    n_list = list(reversed(n_list))
    idx = []
    for j in range(len(n_list)):
        if n_list[j] == '1':
            idx.append(j)

    for k in idx:
        print(k, end=' ')

