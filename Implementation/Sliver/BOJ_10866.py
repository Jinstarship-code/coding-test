from collections import deque

n = int(input())
dq = deque([])
arr = []

for _ in range(n):
  string = input()
  if 'push_back' in string:
    a, b = string.split()
    dq.append(int(b))
  elif 'push_front' in string:
    a, b = string.split()
    dq.appendleft(int(b))
  elif 'pop_front' in string:
    if len(dq) == 0:
      arr.append(-1)
    else:
      arr.append(dq.popleft())
  elif 'pop_back' in string:
    if len(dq) == 0:
      arr.append(-1)
    else:
      arr.append(dq.pop())
  elif 'size' == string:
    arr.append(len(dq))
  elif 'empty' == string:
    if len(dq) == 0:
      arr.append(1)
    else:
      arr.append(0)
  elif 'front' == string:
    if len(dq) == 0:
      arr.append(-1)
    else:
      arr.append(dq[0])
  elif 'back' == string:
    if len(dq) == 0:
      arr.append(-1)
    else:
      arr.append(dq[-1])

for i in range(len(arr)):
  print(arr[i])
