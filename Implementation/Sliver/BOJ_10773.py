import sys

k = int(sys.stdin.readline())

arr = []

for _ in range(k):
  n = int(sys.stdin.readline())
  if n != 0:
    arr.append(n)
  else:
    arr.pop()

print(sum(arr))


"""
구현하기 쉬운 문제
다만, input()을 쓰면 시간초과가 난다.

"""