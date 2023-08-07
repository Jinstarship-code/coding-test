# BOJ_16435

n,l = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()
for i in range(len(arr)):
  if l >= arr[i]:
    l +=1
  else:
    break
print(l)

"""
  쉬운 문제.

  뱀의 길이(l)가 주어지고나서. arr를 오름차순으로 정렬한뒤
  앞에서부터 하나하나씩 먹어나가면 된다.

"""