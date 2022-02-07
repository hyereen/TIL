n = int(input())
j = n-1
s = 1

for i in range(1, n+1):
  star = "*"
  blank = " "
  print(blank*j+star*(i*2-1))
  j -=1
j = 0
for i in range(n-1, 0, -1):
  j +=1
  star = "*"
  blank = " "
  print(blank*j+star*(i*2-1))