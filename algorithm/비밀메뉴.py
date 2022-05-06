import sys

M, N, K = map(int, input().split())

secret_keys = input()

user_input = input()



if secret_keys in user_input:
    print("secret")
else:
    print("normal")