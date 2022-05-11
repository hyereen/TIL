# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq


def solution(scoville, K):
    answer = 0
    scoville.sort()

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        else:

            small = heapq.heappop(scoville)
            small2 = heapq.heappop(scoville)
            heapq.heappush(scoville, (small + (small2 * 2)))
            answer += 1

    return answer