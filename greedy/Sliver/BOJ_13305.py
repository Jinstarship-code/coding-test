import sys

n = int(sys.stdin.readline())
distances = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

min_price = prices[0]
answer = 0
for i in range(n-1):
  if min_price > prices[i]:
    min_price = prices[i]
  answer += min_price * distances[i]

print(answer)

"""
  매 거리마다 가격을 계산해주는데,
  기름값만 min을 유지하면서 계산해주면 된다.

  

"""
