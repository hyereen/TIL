# -*- coding: utf-8 -*-
"""6603.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K3KIOCiXMnHSHdCzxdb_YIYG-YgL4lBN
"""

answer = []

def dfs(idx, list, s, t):
  if len(list) == 6:
    answer.append(list[:])
    return 
  
  for i in range(idx, t):
    dfs(i+1, list+[s[i]], s, t)

while True:
  s = list(map(int, input().split()))
  t = s.pop(0)
  if t == 0:
    break

  dfs(0, [], s, t)
  for i in answer:
    for j in i:
      print(j, end=' ')
    print( )
  print( )

  answer.clear()

answer
