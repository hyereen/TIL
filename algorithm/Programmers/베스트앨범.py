#

# 처음 풀이
# 실패: 테케 2, 15
# 실패 이유: 3번에서 같은 재생횟수더라도, 장르를 구분할 수 없어서 장르 내에서 고유번호가 낮은걸 찾을 수 없음

def solution(genres, plays):
    answer = []
    music = {}
    music_num = {}

    for i in genres:
        music[i] = []

    for i in range(len(plays)):
        music_num[plays[i]] = []

    for i in range(len(plays)):
        music_num[plays[i]] += [i]

    for g, p in zip(genres, plays):
        music[g] += [p]

    # 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    for i in music.keys():
        music[i] = sorted(music[i], reverse=True)

    # 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    music = sorted(music.items(), key=lambda item: sum(item[1]), reverse=True)
    temp = []
    for i in range(len(music)):
        # print(music[i][1][:2])
        temp = temp + music[i][1][:2]

    # print(music_num)
    for i in temp:
        # 3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
        if len(music_num[i]) > 1:
            answer.append(min(music_num[i]))
        else:
            answer.append(music_num[i][0])
    return answer

# 정답
def solution(genres, plays):
    answer = []
    music_all = {}
    music_all_reverse = {}
    genres_nums = {}
    genres_sum = []

    # 모든 노래 트랙 순서대로 번호, 장르, 재생횟수
    for i in range(len(plays)):
        music_all[i] = [genres[i], plays[i]]
        music_all_reverse[genres[i], plays[i]] = []
        genres_nums[genres[i]] = []

    # 장르, 재생횟수랑 트랙순서를 반대로 해서 장르, 재생횟수를 알면 트랙번호를 뽑을려고 만듦
    for i in range(len(plays)):
        music_all_reverse[genres[i], plays[i]] += [i]

    # 장르별 재생횟수
    for k, v in music_all.items():
        genres_nums[v[0]] += [v[1]]

    # 장르별 재생횟수 value 내림차순
    for k, v in genres_nums.items():
        genres_nums[k] = sorted(genres_nums[k], reverse=True)

    # 장르별 재생횟수의 합
    for k, v in genres_nums.items():
        genres_sum.append([k, sum(v)])

        # 장르별 재생횟수의 합 내림차순
    genres_sum.sort(key=lambda x: x[1], reverse=True)

    # print(music_all)
    # print(genres_nums)
    print(genres_sum)
    # print(music_all_reverse)
    for i in genres_sum: # 전체 장르중에서
        genre = i[0]
        for k, v in genres_nums.items(): # 장르별 재생횟수를 봐야되는데
            if genre == k:
                for j in v[:2]: # 재생횟수 중 상위 2개 씩만 봄
                    t = music_all_reverse[k, j] # 그때 장르, 재생횟수에 해당하는 트랙번호를 저장
                    if len(t) > 1: # 같은 장르, 같은 재생횟수인 경우가 2개 이상이라면
                        answer.append(t[0]) # 트랙번호가 작은 값 먼저 넣고
                        t.remove(t[0]) # 작은걸 삭제해줘야 그 다음 작은게 정답에 들어갈 수 있음
                    else:
                        answer.append(t[0]) # 그런 경우가 아니라면 1개 트랙번호를  바로 답에 저장

    return answer

# 참고: https://programmers.co.kr/questions/19664
# https://programmers.co.kr/questions/13110