n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for _ in range(m):
  arr[0], arr[1] = arr[0] + arr[1], arr[0] + arr[1]
  arr.sort()

print(sum(arr))
"""
합이 제일 적은 수를 입력해야하니
arr를 sort()하고 나서 
arr[0],arr[1]에 각각 둘을 더한 값을 넣어준뒤 다시 sort()하는 행동을 m번 반복해서 
sum을 출력하면 최소합이 도출된다.

"""
