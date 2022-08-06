# https://www.acmicpc.net/problem/10988

word = input()
ans = 0

for i in range(len(word)):
    if word[i] != word[len(word)-1-i]: # 첫번째와 마지막단어, 두번째와 마지막에서 두번째 단어들을 비교
        ans = 1
        print('0')
        break
if ans == 0:
    print('1')
