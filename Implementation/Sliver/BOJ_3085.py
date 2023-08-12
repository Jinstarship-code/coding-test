#BOJ_3085

n = int(input())
maxCount = 0

arr = []
for _ in range(n):
  tmp = input()
  tmp = list(tmp[::1])
  arr.append(tmp)


def Row():
  global maxCount

  for i in range(n):
    countRow = 1
    for j in range(n - 1):
      if arr[i][j] == arr[i][j + 1]:
        countRow += 1
        maxCount = max(maxCount, countRow)
      else:
        countRow = 1


def Column():
  global maxCount
  for i in range(n):
    countColumn = 1
    for j in range(n - 1):
      if arr[j][i] == arr[j + 1][i]:
        countColumn += 1
        maxCount = max(maxCount, countColumn)
      else:
        countColumn = 1


for i in range(n):
  for j in range(n - 1):
    if arr[i][j] != arr[i][j + 1]:
      arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
      Row()
      Column()
      arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

    if arr[j][i] != arr[j + 1][i]:
      arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
      Row()
      Column()
      arr[j + 1][i], arr[j][i] = arr[j][i], arr[j + 1][i]

print(maxCount)

"""
배열의 크기가 작아 시간복잡도 신경쓰지 않고 머릿속에 구현하는 대로 작성하면 된다.
나같은 경우 row와 column으로 함수를 만들어서 변경했을때 maxCount를 구하는 식으로 작성하였다.

"""