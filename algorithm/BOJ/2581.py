# -*- coding: utf-8 -*-
"""2581.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jz6Q3MvMCEQmAMJemSDpLml1obTj71_9
"""

m = int(input())
n = int(input())
sosus=[]

def is_sosu(x):
  divisors = 0
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      divisors +=1
  
  if divisors != 0:
    return False
  else:
    return True

for i in range(m, n+1):
  if is_sosu(i):
    sosus.append(i)

if len(sosus) == 0:
  print(-1)
else:
  print(sum(sosus))
  print(min(sosus))