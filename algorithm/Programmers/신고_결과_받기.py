# https://programmers.co.kr/learn/courses/30/lessons/92334

# 맨 처음 풀이
# 시간초과: 테케 3, 11, 15, 21

def solution(id_list, report, k):
    answer = []
    do_singo = []
    get_singo = []
    for i in range(len(id_list)):
        do_singo.append([])
        get_singo.append([])
        answer.append(0)
    for i in range(len(report)):
        f, t = report[i].split()
        for j in range(len(id_list)):
            if id_list[j] == f and t not in do_singo[j]:
                do_singo[j].append(t)
            if id_list[j] == t and f not in get_singo[j]:
                get_singo[j].append(f)
    # print(get_singo, do_singo)
    for i in range(len(get_singo)):
        if len(get_singo[i]) >= k:
            for j in range(len(id_list)):
                if id_list[i] in do_singo[j]:
                    answer[j] = answer[j] + 1

    # print(answer)
    return answer

# 시간초과: 테케 3, 11
def solution(id_list, report, k):
    answer = {}
    do_singo = {}
    get_singo = {}

    for user in id_list:
        do_singo[user] = []
        get_singo[user] = []
        answer[user] = 0

    for i in report:
        f, t = i.split()
        # print("f,t", f,t )
        for j in id_list:
            if j == f and t not in do_singo[j]:
                do_singo[j].append(t)
            if j == t and f not in get_singo[j]:
                get_singo[j].append(f)
    # print(get_singo, do_singo)
    for do, get in get_singo.items():
        if len(get_singo[do]) >= k:
            for d, g in do_singo.items():
                # print(do, d, g)
                if do in g:
                    answer[d] += 1

    # print(answer)
    # print(list(answer.values()))
    return list(answer.values())


# 통과
# report를 살펴보는 for문에서 dict니까 이중 포문이 필요하지 않아서 삭제하고, 따라서 if문도 간결해짐 !
def solution(id_list, report, k):
    answer = {}
    do_singo = {}
    get_singo = {}

    for user in id_list:
        do_singo[user] = []
        get_singo[user] = []
        answer[user] = 0

    for i in report:
        f, t = i.split()
        # print("f,t", f,t )
        if t not in do_singo[f]:
            do_singo[f].append(t)
        if f not in get_singo[t]:
            get_singo[t].append(f)
    # print(get_singo, do_singo)
    for do, get in get_singo.items():
        if len(get_singo[do]) >= k:
            for d, g in do_singo.items():
                # print(do, d, g)
                if do in g:
                    answer[d] += 1

    # print(answer)
    # print(list(answer.values()))
    return list(answer.values())