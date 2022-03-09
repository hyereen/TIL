a, b = map(int, input().split())

# 약수 구하기
def get_divs(a):
    divs = []
    for i in range(1, a+1):
        if a % i == 0:
            divs.append(i)
    return divs

# 최대공약수 구하기
def get_gcd(divs1, divs2):
    return max(list(set(divs1).intersection(set(divs2))))


a_divs = get_divs(a)
b_divs = get_divs(b)

# 최대공약수 출력
gcd = get_gcd(a_divs, b_divs)
print(gcd)
# 최소공배수 출력 = 최소공배수는 두 수의 곱 나누기 두 수의 최대공약수
lcm = a*b/gcd
print(format(lcm, ".0f"))