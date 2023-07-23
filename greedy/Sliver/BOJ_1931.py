n = int(input())

arr = []
for i in range(n):
  a, b = map(int, input().split())
  arr.append((a, b))

arr = sorted(arr, key=lambda x: (x[1], x[0]))

cnt = 1
b = arr[0][1]
for i in range(1,len(arr)):
  if b > arr[i][0]:
    continue
  cnt += 1
  b = arr[i][1]
  

print(cnt)
"""
1개의 회의실 <- n개의 회의
겹치지 않으면서 사용할수있는 회의의 최대개수

  풀이 방법:
    1. 종료시간이 작은 순서대로 정렬 후 시작시간도 오른차순으로 정렬
    2. 현재 종료시간 <= 다음 시작시간 인 부분은 찾아 cnt += 1 해준다.
      - 정렬되어 있는 상태라 지금 계산한 것이 제일 max된 경우의 수가 된다.
"""
