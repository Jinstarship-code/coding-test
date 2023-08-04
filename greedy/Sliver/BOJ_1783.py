# BOJ_1783 병든 나이트

import sys

n, m = map(int, sys.stdin.readline().strip().split())

if n == 1:
  print(1)
elif n == 2:
  if m >= 7:
    print(4)
  else:
    if m <= 2:
      print(1)
    elif m <= 4:
      print(2)
    elif m <= 6:
      print(3)
else:
  if m >= 7:
    print(m - 2)
  else:
    if m <= 4:
      print(m)
    else:
      print(4)
"""
경우의 수를 머리 속으로 풀어서 답을 맞추는 문제

(1) 2칸 위로, 1칸 오른쪽
(2) 1칸 위로, 2칸 오른쪽
(3) 1칸 아래로, 2칸 오른쪽
(4) 2칸 아래로, 1칸 오른쪽

n이 1인 경우는 못움직임 따라서 1이 답
n = 2 인 경우, 2,4번 방법 밖엔 움질일수 없어서 방문횟수가 4가 max
  m = 1 -> 1
  m = 2 -> 1
  m = 3 -> 2
  m = 4 -> 2
  m = 5 -> 3
  m = 6 -> 3
  m >= 7 -> 4

n >= 3
  첫번째
  m = 1 -> 1
  m = 2 -> 2
  m = 3 -> 3
  m = 4 -> 4
  
  두번째(1,3후 2,4)
  . . . . . . . 
  . . . . . . . 
  . . . . . . . 
  . . . . . . . 
  m = 5 -> 4
  m = 6 -> 4
  m >= 7 -> m -2

  세번재(2,4후 1,3)
  m = 5 -> 3
  m = 6 -> 4
  m >= 7 -> m-2
"""
