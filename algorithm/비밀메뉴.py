# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=623

M, N, K = map(int, input().split())

secret_keys = input()

user_input = input()



if secret_keys in user_input:
    print("secret")
else:
    print("normal")