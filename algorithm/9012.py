# -*- coding: utf-8 -*-
"""9012.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/132vQEgx0_9hbIrwqd1iHdkvFAIWjZL5u
"""

t = int(input())

for i in range(0, t):
  ps_str = input()
  for i in range(0, len(ps_str)):
    ps_str = ps_str.replace('()', '')

  if len(ps_str) == 0:
    print("YES")
  else:
    print("NO")
