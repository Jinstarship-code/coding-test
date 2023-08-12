#BOJ_2740

n, m = map(int, input().split())

arr1 = []
for _ in range(n):
  arr1 += [list(map(int, input().split()))]
arr2 = []
m, k = map(int, input().split())
for _ in range(m):
  arr2 += [list(map(int, input().split()))]

answer = []


# 행렬의 인덱스의 값을 계산해주는 함수
def MatrixMul(i, j):
  tmp1 = []
  tmp2 = []
  # 각 행렬의 계산 하는 부분들을 tmp1과 tmp2에 나눠서 담음
  for t in range(m):
    tmp1.append(arr1[i][t])
    tmp2.append(arr2[t][j])
  tmp = 0

  # 행렬 곱셈
  for t in range(len(tmp1)):
    tmp += tmp1[t] * tmp2[t]
  return tmp


for i in range(n):
  for j in range(k):
    print(MatrixMul(i, j), end=' ')
  if i != n - 1:
    print()
"""
  
  나의 풀이의 경우 만들어지는 행렬(n x k)의 인덱스를 하나하나씩 계산해주는 함수를 만들었다.
  
"""
