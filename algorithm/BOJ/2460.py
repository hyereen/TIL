people = 0
max_pp = 0
for i in range(10):
  off, on = map(int, input().split())
  people = people - off + on
  if people > max_pp:
      max_pp = people

print(max_pp)