# -*- coding: utf-8 -*-
"""정렬.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QVNoz1i5fiXmcQppxBF9cXmGBPw6Xzrp
"""

# 6-1.py 선택정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_idx = i
  for j in range(i+1, len(array)):
    if array[min_idx] > array[j]:
      min_idx = j
  array[i], array[min_idx] = array[min_idx], array[i]

print(array)