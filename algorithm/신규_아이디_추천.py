# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    special = ['-', '_', '.', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', '{', '}', ':', '?',
               ',', '<', '>', '/']

    # 1단계
    answer = new_id.lower()
    # 2단계
    special = answer.maketrans({'~': '',
                                '!': '',
                                '@': '',
                                '#': '',
                                '$': '',
                                '%': '',
                                '^': '',
                                '&': '',
                                '*': '',
                                '(': '',
                                ')': '',
                                '=': '',
                                '+': '',
                                '[': '',
                                ']': '',
                                '{': '',
                                '}': '',
                                ':': '',
                                '?': '',
                                ',': '',
                                '<': '',
                                '>': '',
                                '/': ''})
    answer = answer.translate(special)

    # 3단계
    answer = answer.replace('...............', '.', 15)
    answer = answer.replace('..............', '.', 15)
    answer = answer.replace('.............', '.', 15)
    answer = answer.replace('............', '.', 15)
    answer = answer.replace('...........', '.', 15)
    answer = answer.replace('..........', '.', 15)
    answer = answer.replace('.........', '.', 15)
    answer = answer.replace('........', '.', 15)
    answer = answer.replace('.......', '.', 15)
    answer = answer.replace('......', '.', 15)
    answer = answer.replace('.....', '.', 15)
    answer = answer.replace('....', '.', 15)
    answer = answer.replace('...', '.', 15)
    answer = answer.replace('..', '.', 15)

    # 4단계
    answer = answer.strip(".")

    # 5단계
    if not answer:
        answer = "a"

    # 6단계
    answer = answer[:15]
    answer = answer.rstrip('.')

    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1:]

    return answer