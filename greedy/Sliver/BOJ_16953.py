import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 1
while True:
  if b == a:
    break
  elif (b % 2 != 0 and b % 10 != 1) or (b < a):
    cnt = -1
    break
  else:
    if b % 10 == 1:
      b = b // 10
    elif b % 2 == 0:
      b = b // 2
    cnt += 1

print(cnt)

"""
    문제 분류가 그리디랑 bfs로 되어있다.
    나의 풀이는 그리디로 푼것을 적었다.

    # bfs 풀이(ctrl + c,v)

    from collections import deque

    a,b = map(int,input().split())
    res = -1
    que = deque([(a,1)])
    while que:
        i, cnt = que.popleft()
        if i == b:
            res = cnt
            break

        if i*2 <= b:
            que.append((i*2,cnt+1))
        if int(str(i)+'1') <= b:
            que.append((int(str(i)+'1),cnt+1))

    print(res)


"""
