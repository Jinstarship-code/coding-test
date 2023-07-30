n = int(input())

arr = []
for _ in range(n):
  arr += [list(map(int, input().split()))]
idx = max(max(arr)) + 10
background = [[0] * 100 for _ in range(100)]

# 배열에 1씩 더해서 검은색색종이의 영역 추가
for i in range(len(arr)):
  a, b = arr[i]
  for j in range(a, a + 10):
    for k in range(b, b + 10):
      background[j][k] += 1

# background[i][j] >= 1 세기
cnt = 0
for i in range(100):
  for j in range(100):
    if background[i][j]:
      cnt += 1
print(cnt)
"""

  100*100인 흰도화지를 하나 만들어서
  검은색 영역을 +1씩 해주고 나서
  1이상인 배열을 세어주면 된다.

"""
