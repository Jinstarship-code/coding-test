# BOJ_11501
import sys

for _ in range(int(sys.stdin.readline().strip())):
  n = int(sys.stdin.readline().strip())
  arr = list(map(int, sys.stdin.readline().strip().split()))
  max = 0
  profit = 0

  for i in range(len(arr) - 1, -1, -1):
    if arr[i] > max:
      max = arr[i]
    else:
      profit += max - arr[i]
  print(profit)
  """
    이 문제의 경우 앞에서 부터 풀게되면 시간초과에 걸리게 된다.

    뒤에서 부터 풀게되면 max값만 변화시키면서, 그날그날의 가격을 팔아버리게 되기때문에 시간초과 없이 편하게 풀수 있다.
  """
