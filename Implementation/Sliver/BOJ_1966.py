from collections import deque

answer = []
for _ in range(int(input())):
  n, m = map(int, input().split())

  if n == 1:
    tmp = int(input())
    answer.append(1)
    continue

  queue = deque(map(int, input().split()))
  cnt = 0
  max_queue = max(queue)
  while True:
    m -= 1
    p = queue.popleft()
    if p == max_queue and m == -1:
      cnt += 1
      answer.append(cnt)
      break
    elif p == max_queue:
      max_queue = max(queue)
      cnt += 1
      continue

    if p != max_queue:
      queue.append(p)
      if m < 0:
        m = len(queue) - 1

for a in answer:
  print(a)
"""
  python의 deque를 이용하면 쉽게 풀수 있는 문제.
  중요도를 체크하면서 while을 돌리면 간단하게 답을 도출해낼수 있다.

"""
