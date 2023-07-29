n, m = map(int, input().split())


def ChangeMatrix(arr, n, m):
  for i in range(n, n + 3):
    for j in range(m, m + 3):
      if arr[i][j] == 1:
        arr[i][j] = 0
      elif arr[i][j] == 0:
        arr[i][j] = 1

  return arr


tmp1 = []
tmp2 = []
before = [[0] * m for _ in range(n)]
after = [[0] * m for _ in range(n)]
for _ in range(n):
  tmp1.append(list(map(str, input())))
for _ in range(n):
  tmp2.append(list(map(str, input())))

# 행렬 변환 (str -> int)
for i in range(n):
  for j in range(m):
    if tmp1[i][j] == '1':
      before[i][j] = 1

    if tmp2[i][j] == '1':
      after[i][j] = 1
cnt = 0
# 행렬 체크
if n < 3 or m < 3:
  if before == after:
    print(0)
  else:
    print(-1)
else:
  for i in range(n - 2):
    for j in range(m - 2):
      if before[i][j] != after[i][j]:
        before = ChangeMatrix(before, i, j)
        cnt += 1

  if before != after:
    print(-1)
  else:
    print(cnt)
"""
  1. 먼저 ChangeMatrix()라는 함수를 생성(3*3 행렬 뒤집어주는 역할)
  2. input을 받고 str을 int로 바꿔주는 list를 하나더 만들었다.
  3. 이중 for문을 돌면서 바꿔주는 작업을 진행했다.
  만약 다돌았는데 다르면 애초에 못바꾸므로 -1을 출력

  (주의)
    n<3, m<3인 조건에선 행렬을 뒤집을 수 없으므로 -1이 출력되어야 겠다고 생각하겠지만, 처음부터 행렬 A와 B가 동일하다면?
    그럼 바꿀필요가 없으니 0을 출력해야한다.

"""
