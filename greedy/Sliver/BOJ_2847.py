n = int(input())

arr = []
for i in range(n):
  arr.append(int(input()))
arr = arr[-1::-1]

cnt = 0
for i in range(n - 1):
  if arr[i] <= arr[i + 1]:
    cnt += arr[i + 1] - arr[i] + 1
    arr[i + 1] = arr[i] - 1

print(cnt)
"""
풀이의 핵심: 내림차순으로 정렬하고 뒤에서부터 값을 정리해나가는 것이 좋다.

"""
